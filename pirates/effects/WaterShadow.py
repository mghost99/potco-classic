from pandac.PandaModules import *
from otp.otpbase import OTPRender
from libpirates import SeaPatchNode

class WaterShadow(NodePath):

    def __init__(self, name, shadow_model, parent, use_water_bin = True, bin_number = 7):
        self.use_water_bin = use_water_bin
        self.bin_number = bin_number
        self.shadow_model = shadow_model
        if self.shadow_model:
            if hasattr(base, 'pe'):
                shadow_spn = SeaPatchNode('water_shadow_spn', base.pe.seaPatch.patch)
            else:
                shadow_spn = SeaPatchNode('water_shadow_spn', base.cr.activeWorld.getWater().patch)
            shadow_spn.setWantColor(0)
            shadow_spn.setWantUv(0)
            shadow_spn.setWantNormal(0)
            shadow_spn.setWantReflect(0)
            NodePath.__init__(self, shadow_spn)
            self.name = name
            self.shadow_model.reparentTo(self)
            shadow_spn.collectGeometry()
            if self.use_water_bin:
                self.setBin('water', self.bin_number)
                self.setDepthWrite(0)
            else:
                self.setBin('ground', -2)
            self.setDepthTest(0)
            self.setLightOff()
            self.reparentTo(parent)
            OTPRender.renderReflection(False, self, 'p_water_shadow', None)
            if hasattr(base, 'pe'):
                shadow_spn.setEffect(CompassEffect.make(base.pe.seaPatch.patchNP, CompassEffect.PZ))
            else:
                shadow_spn.setEffect(CompassEffect.make(base.cr.activeWorld.getWater().patchNP, CompassEffect.PZ))
            if self.use_water_bin:
                mask = 0xFFFFFFFF
                stencil = StencilAttrib.make(1, StencilAttrib.SCFEqual, StencilAttrib.SOKeep, StencilAttrib.SOKeep, StencilAttrib.SOKeep, 1, mask, mask)
                self.setAttrib(stencil)
