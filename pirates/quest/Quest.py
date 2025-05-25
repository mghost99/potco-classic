from direct.directnotify import DirectNotifyGlobal
from direct.showbase.PythonUtil import POD, makeTuple
from direct.task.Task import Task
from pirates.piratesbase import PLocalizer
from pirates.quest import QuestDB, QuestReward, QuestTaskDNA
from pirates.quest.QuestDNA import QuestDNA
from otp.otpbase import OTPGlobals
from pirates.piratesbase import Freebooter

class Quest(POD):
    notify = DirectNotifyGlobal.directNotify.newCategory('Quest')
    DataSet = {
        'questId': None,
        'giverId': None,
        'combineOp': None,
        'tasks': None,
        'rewards': None,
        'taskStates': []}
    SerialNum = 0

    def __init__(self, questId = None, giverId = None, initialTaskStates = None, rewards = None):
        self.questDNA = None
        self._serialNum = Quest.SerialNum
        Quest.SerialNum += 1
        POD.__init__(self)
        if questId is not None:
            self.setupQuest(questId, giverId, initialTaskStates, rewards)

        self.__finished = False
        self.__finalized = False

    def destroy(self):
        del self.questDNA
        del self.tasks
        del self.rewards
        for taskState in self.taskStates:
            taskState.release()

        del self.taskStates

    def setupQuest(self, questId, giverId, initialTaskStates, rewards):
        self.setQuestId(questId)
        self.setGiverId(giverId)
        self.setRewards(rewards)
        self.sendTaskStates(initialTaskStates)

    def setQuestId(self, questId):
        self.questId = questId
        if questId not in (None, ''):
            self.questDNA = QuestDB.QuestDict.get(self.questId)
            if self.questDNA:
                self.questDNA.makeCopy()
                self.setCombineOp(self.questDNA.getCombineOp())
                self.setTasks(self.questDNA.getTasks())

        else:
            self.questDNA = None

    def getQuestDNA(self):
        return self.questDNA

    def getQuestGoalUid(self):
        for (taskState, taskDNA) in zip(self.taskStates, self.questDNA.getTasks()):
            return taskDNA.getGoalUid()
        return None

    def getChangeEvent(self):
        return 'Quest.questChange-%s' % self._serialNum

    def setTaskStates(self, taskStates):
        oldTaskStates = getattr(self, 'taskStates', None)
        self.taskStates = taskStates
        if self.taskStates:
            for taskState in self.taskStates:
                taskState.acquire()

        if oldTaskStates:
            for taskState in oldTaskStates:
                taskState.release()

        messenger.send(self.getChangeEvent())

    def sendTaskStates(self, taskStates):
        self.setTaskStates(taskStates)

    def setRewardStructs(self, rewardStructs):
        rewards = []
        for rewardStruct in rewardStructs:
            rewards.append(QuestReward.QuestReward.makeFromStruct(rewardStruct))

        self.setRewards(rewards)

    def getRewardStructs(self):
        rewardStructs = []
        for reward in self.getRewards():
            rewardStructs.append(reward.getQuestRewardStruct())

        return rewardStructs

    def handleEvent(self, holder, questEvent):
        modified = 0
        for (taskState, taskDNA) in zip(self.taskStates, self.questDNA.getTasks()):
            if taskDNA.locationMatches(questEvent):
                taskState.resetModified()
                if questEvent.applyTo(taskState, taskDNA):
                    if holder.getAccess() != 2 and self.questDNA.getVelvetRoped():
                        holder.d_popupProgressBlocker(self.getQuestId())
                    else:
                        questEvent.complete(taskState, taskDNA)

                modified += taskState.isModified()

        if modified:
            self.sendTaskStates(self.taskStates)

    def isDroppable(self):
        return self.questDNA.getDroppable()

    def isShareable(self):
        return True

    def completeRequiresVisit(self):
        return self.questDNA.getCompleteRequiresVisit()

    def playStinger(self):
        if not self.questDNA:
            return False

        return self.questDNA.getPlayStinger()

    def setFinalized(self):
        self.__finalized = True

    def isFinalized(self):
        return self.__finalized

    def isComplete(self, showComplete = False):
        if self.__finished:
            return True

        if hasattr(self, 'taskStates'):
            if len(self.taskStates) == 0:
                return True

        else:
            return False
        if self.combineOp is QuestDNA.OR:
            for task in self.taskStates:
                if task.isComplete():
                    self.__finished = True
                    return True

            return False
        elif self.combineOp is QuestDNA.AND:
            for task in self.taskStates:
                if not task.isComplete():
                    return False

            self.__finished = True
            return True
        else:
            raise 'unknown task combineOp: %s' % self.combineOp

    def percentComplete(self):
        if self.__finished or self.isComplete() == True:
            return 1.0

        if hasattr(self, 'taskStates') and len(self.taskStates) == 0:
            return 1.0

        if self.combineOp is QuestDNA.OR:
            return 0.0
        elif self.combineOp is QuestDNA.AND:
            totalTasks = len(self.taskStates)
            completedTasks = 0
            for task in self.taskStates:
                if task.isComplete():
                    completedTasks += 1

            return completedTasks / totalTasks
        else:
            raise 'unknown task combineOp: %s' % self.combineOp


    def canBeReturnedTo(self, giverId):
        if not self.isComplete():
            pass

        noGiversSpecified = True
        returnGiverIds = self.questDNA.getReturnGiverIds()
        if returnGiverIds is not None:
            noGiversSpecified = False
            if giverId in returnGiverIds:
                return True

        for (task, taskState) in zip(self.getTasks(), self.getTaskStates()):
            if taskState.isComplete():
                returnGiverIds = task.getReturnGiverIds()
                if returnGiverIds is not None:
                    noGiversSpecified = False
                    if giverId in returnGiverIds:
                        return True

        if noGiversSpecified:
            if giverId == self.getGiverId():
                return True

        return False

    def getSCSummaryText(self, taskNum):
        return self.questDNA.getSCSummaryText(taskNum)

    def getSCWhereIsText(self, taskNum):
        return self.questDNA.getSCWhereIsText(taskNum)

    def getSCHowToText(self, taskNum):
        return self.questDNA.getSCHowToText(taskNum)

    def getDescriptionText(self):
        return self.questDNA.getDescriptionText(self.taskStates)

    def getRewardText(self):
        return QuestReward.QuestReward.getDescriptionText(self.getRewards())

    def getReturnText(self):
        choice = False
        choiceComplete = False
        container = localAvatar.questStatus.getContainer(self.questId)
        if container and container.parent and container.parent.isChoice():
            choice = True
            if container.parent.getComplete():
                choiceComplete = True

        returnGiverIds = self.questDNA.getReturnGiverIds()
        if returnGiverIds:
            npcNames = [PLocalizer.NPCNames.get(id, PLocalizer.DefaultTownfolkName) for id in returnGiverIds]
            if len(returnGiverIds) == 1:
                if choice and not choiceComplete:
                    return PLocalizer.SingleChoiceQuestReturnId % {
                        'npcName': npcNames[0]}
                else:
                    return PLocalizer.SingleQuestReturnId % {
                        'npcName': npcNames[0]}
            elif choice and not choiceComplete:
                return PLocalizer.MultipleChoiceQuestReturnIds % {
                    'npcNames': npcNames}
            else:
                return PLocalizer.MultipleQuestReturnIds % {
                    'npcNames': npcNames}
        else:
            giverId = ''
            if self.getGiverId() != '1152839242.37jubutler':
                giverId = self.getGiverId()

            if giverId == '' or giverId == '0':
                taskDNAs = self.questDNA.getTaskDNAs()
                for task in taskDNAs:
                    if isinstance(task, QuestTaskDNA.VisitTaskDNA):
                        giverId = task.getReturnGiverIds()[0]
                        break

            npcName = PLocalizer.NPCNames.get(giverId, PLocalizer.DefaultTownfolkName)
            if choice and not choiceComplete:
                return PLocalizer.SingleChoiceQuestReturnId % {
                    'npcName': npcName}
            else:
                return PLocalizer.SingleQuestReturnId % {
                    'npcName': npcName}

    def getTaskProgress(self):
        progressList = []
        taskStates = getattr(self, 'taskStates', None)
        if taskStates:
            for taskState in taskStates:
                goal = taskState.getGoal()
                progress = taskState.getProgress()
                progressList.append((progress, goal))

        return progressList

    def getStatusText(self):
        if self.questDNA.getVelvetRoped() and base.localAvatar.getAccess() != OTPGlobals.AccessFull:
            if not Freebooter.AllAccessHoliday:
                return PLocalizer.VelvetRopeQuestBlock

        taskDNAs = self.questDNA.getTaskDNAs()
        taskStates = self.getTaskStates()

        def getTaskText(taskDNA, taskState, format):
            goal = taskState.getGoal()
            progress = taskState.getProgress()
            progressStr = ''
            if progress < goal:
                if goal > 1:
                    progressStr = PLocalizer.QuestTaskProgress % {
                        'prog': progress,
                        'goal': goal}

            else:
                progressStr = PLocalizer.QuestProgressComplete
            return format % {
                'task': taskDNA.getDescriptionText(taskState),
                'prog': progressStr}

        if len(taskDNAs) == 1:
            str = PLocalizer.QuestStrOneTask % {
                'task': getTaskText(taskDNAs[0], taskStates[0], PLocalizer.QuestStatusTaskSingle)}
        else:
            headingStr = {
                QuestDNA.OR: PLocalizer.QuestMultiHeadingOr,
                QuestDNA.AND: PLocalizer.QuestMultiHeadingAnd}[self.getCombineOp()]
            tasksStr = ''
            for (taskDNA, taskState) in zip(taskDNAs, taskStates):
                tasksStr += getTaskText(taskDNA, taskState, PLocalizer.QuestStatusTaskMulti)

            str = PLocalizer.QuestStrMultiTask % {
                'heading': headingStr,
                'tasks': tasksStr}
        return str

    def __repr__(self):
        return '<Quest %s>' % self.getQuestId()

    def handleStart(self, avId):
        for currTask in self.tasks:
            currTask.handleStart(avId)
