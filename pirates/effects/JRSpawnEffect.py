from pandac.PandaModules import *
from direct.interval.IntervalGlobal import *
from direct.particles import ParticleEffect
from direct.particles import Particles
from direct.particles import ForceGroup
from .EffectController import EffectController
from .PooledEffect import PooledEffect
import random

class JRSpawnEffect(PooledEffect, EffectController):
    card2Scale = 64.0
    cardScale = 64.0
    
    def __init__(self, parent = None):
        PooledEffect.__init__(self)
        EffectController.__init__(self)
        if parent is not None:
            self.reparentTo(parent)
        
        if not JRSpawnEffect.particleDummy:
            JRSpawnEffect.particleDummy = render.attachNewNode(ModelNode('JRSpawnEffectParticleDummy'))
            JRSpawnEffect.particleDummy.setColorScaleOff()
            JRSpawnEffect.particleDummy.setLightOff()
            JRSpawnEffect.particleDummy.setFogOff()
            JRSpawnEffect.particleDummy.setDepthWrite(0)
        
        self.effectScale = 1.0
        self.duration = 3.0
        model = loader.loadModel('models/effects/particleMaps')
        self.card = model.find('**/particleEvilSmoke')
        self.card2 = model.find('**/particleWhiteSmoke')
        self.f = ParticleEffect.ParticleEffect('JRSpawnEffect')
        self.f.reparentTo(self)
        self.p0 = Particles.Particles('particles-1')
        self.p0.setFactory('ZSpinParticleFactory')
        self.p0.setRenderer('SpriteParticleRenderer')
        self.p0.setEmitter('DiscEmitter')
        self.p1 = Particles.Particles('particles-2')
        self.p1.setFactory('PointParticleFactory')
        self.p1.setRenderer('SpriteParticleRenderer')
        self.p1.setEmitter('RingEmitter')
        self.f.addParticles(self.p0)
        self.f.addParticles(self.p1)
        f0 = ForceGroup.ForceGroup('Gravity')
        force0 = LinearVectorForce(Vec3(0.0, 0.0, -5.0), 1.0, 0)
        force0.setVectorMasks(1, 1, 1)
        force0.setActive(1)
        f0.addForce(force0)
        self.f.addForceGroup(f0)
        self.p0.setPoolSize(256)
        self.p0.setBirthRate(0.0)
        self.p0.setLitterSize(2)
        self.p0.setLitterSpread(0)
        self.p0.setSystemLifespan(0.0)
        self.p0.setLocalVelocityFlag(1)
        self.p0.setSystemGrowsOlderFlag(0)
        self.p0.factory.setLifespanBase(1.25)
        self.p0.factory.setLifespanSpread(0.0)
        self.p0.factory.setMassBase(1.0)
        self.p0.factory.setMassSpread(0.0)
        self.p0.factory.setTerminalVelocityBase(400.0)
        self.p0.factory.setTerminalVelocitySpread(0.0)
        self.p0.renderer.setAlphaMode(BaseParticleRenderer.PRALPHAINOUT)
        self.p0.renderer.setUserAlpha(0.75)
        self.p0.renderer.setFromNode(self.card)
        self.p0.renderer.setColor(Vec4(1.0, 1.0, 1.0, 1.0))
        self.p0.renderer.setXScaleFlag(1)
        self.p0.renderer.setYScaleFlag(1)
        self.p0.renderer.setAnimAngleFlag(1)
        self.p0.renderer.setNonanimatedTheta(0.0)
        self.p0.renderer.setAlphaBlendMethod(BaseParticleRenderer.PPBLENDLINEAR)
        self.p0.renderer.setAlphaDisable(0)
        self.p0.renderer.setColorBlendMode(ColorBlendAttrib.MAdd, ColorBlendAttrib.OIncomingColor, ColorBlendAttrib.OOne)
        self.p0.renderer.getColorInterpolationManager().addLinear(0.0, 0.5, Vec4(1.0, 1.0, 0.2, 1.0), Vec4(0.8, 0.6, 0.25, 0.75), 1)
        self.p0.renderer.getColorInterpolationManager().addLinear(0.5, 1.0, Vec4(0.8, 0.6, 0.25, 0.75), Vec4(0.5, 0.25, 0.0, 0.5), 1)
        self.p0.emitter.setEmissionType(BaseParticleEmitter.ETRADIATE)
        self.p0.emitter.setAmplitude(1.0)
        self.p0.emitter.setAmplitudeSpread(0.0)
        self.p0.emitter.setOffsetForce(Vec3(0.0, 0.0, 4.0))
        self.p0.emitter.setExplicitLaunchVector(Vec3(1.0, 0.0, 0.0))
        self.p0.emitter.setRadiateOrigin(Point3(0.0, 0.0, 0.0))
        self.p0.emitter.setRadius(0.0)
        self.p1.setPoolSize(256)
        self.p1.setBirthRate(0.01)
        self.p1.setLitterSize(2)
        self.p1.setLitterSpread(0)
        self.p1.setSystemLifespan(0.0)
        self.p1.setLocalVelocityFlag(1)
        self.p1.setSystemGrowsOlderFlag(0)
        self.p1.factory.setLifespanBase(1.8)
        self.p1.factory.setLifespanSpread(0.2)
        self.p1.factory.setMassBase(1.0)
        self.p1.factory.setMassSpread(0.2)
        self.p1.factory.setTerminalVelocityBase(400.0)
        self.p1.factory.setTerminalVelocitySpread(0.0)
        self.p1.renderer.setAlphaMode(BaseParticleRenderer.PRALPHAINOUT)
        self.p1.renderer.setUserAlpha(0.5)
        self.p1.renderer.setFromNode(self.card2)
        self.p1.renderer.setColor(Vec4(1.0, 1.0, 1.0, 1.0))
        self.p1.renderer.setXScaleFlag(1)
        self.p1.renderer.setYScaleFlag(1)
        self.p1.renderer.setAnimAngleFlag(0)
        self.p1.renderer.setNonanimatedTheta(0.0)
        self.p1.renderer.setAlphaBlendMethod(BaseParticleRenderer.PPBLENDLINEAR)
        self.p1.renderer.setAlphaDisable(0)
        self.p1.renderer.getColorInterpolationManager().addLinear(0.0, 1.0, Vec4(0.5, 0.6, 0.15, 1.0), Vec4(0.6, 0.75, 0.0, 0.0), 1)
        self.p1.emitter.setEmissionType(BaseParticleEmitter.ETCUSTOM)
        self.p1.emitter.setAmplitude(2.5)
        self.p1.emitter.setAmplitudeSpread(0.0)
        self.p1.emitter.setOffsetForce(Vec3(0.0, 0.0, 2.0))
        self.p1.emitter.setExplicitLaunchVector(Vec3(0.0, 0.0, 0.0))
        self.p1.emitter.setRadiateOrigin(Point3(0.0, 0.0, 10.0))
        self.p1.emitter.setRadius(0.5)
        self.p1.emitter.setRadiusSpread(0.0)

    def setupSize(self):
        self.p0.renderer.setInitialXScale(0.015 * self.effectScale * self.card2Scale)
        self.p0.renderer.setFinalXScale(0.05 * self.effectScale * self.card2Scale)
        self.p0.renderer.setInitialYScale(0.015 * self.effectScale * self.card2Scale)
        self.p0.renderer.setFinalYScale(0.05 * self.effectScale * self.card2Scale)
        self.p1.renderer.setInitialXScale(0.015 * self.effectScale * self.card2Scale)
        self.p1.renderer.setFinalXScale(0.05 * self.effectScale * self.card2Scale)
        self.p1.renderer.setInitialYScale(0.015 * self.effectScale * self.card2Scale)
        self.p1.renderer.setFinalYScale(0.05 * self.effectScale * self.card2Scale)
        self.p1.emitter.setAmplitude(3.5 * self.effectScale)
    
    def createTrack(self):
        expand = LerpFunctionInterval(self.reSize, 1.0, toData = 1.0, fromData = 0.0)
        shrink = LerpFunctionInterval(self.reSize, 0.75, toData = 0.0, fromData = 1.0)
        moveUp = LerpPosInterval(self, 0.75, Vec3(self.getX(), self.getY(), self.getZ() + 1.0), startPos = self.getPos())
        self.startEffect = Sequence(Func(self.setupSize), Func(self.p0.setBirthRate, 0.01), Func(self.p0.clearToInitial), Func(self.p1.setBirthRate, 0.015), Func(self.p1.clearToInitial), Func(self.f.start, self, self.particleDummy), expand)
        self.endEffect = Sequence(Parallel(moveUp, shrink), Wait(0.25), Func(self.p0.setBirthRate, 100), Func(self.p1.setBirthRate, 100), Wait(2.0), Func(self.cleanUpEffect))
        self.track = Sequence(self.startEffect, Wait(self.duration), self.endEffect)

    def reSize(self, t):
        self.p0.emitter.setRadius(3.0 * t * self.effectScale)
        self.p0.emitter.setRadius(2.0 * t * self.effectScale)

    def cleanUpEffect(self):
        EffectController.cleanUpEffect(self)
        if self.pool.isUsed(self):
            self.pool.checkin(self)

    def destroy(self):
        EffectController.destroy(self)
        PooledEffect.destroy(self)


