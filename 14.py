class Robot:
    def __init__(self, name, battery=100, state="idle"):
        self.name = name
        self.battery = battery
        self.state = state

    def status(self):
        data = [self.name, self.battery, self.state]
        return data

    def info(self):
        return f"Robot {self.name} ready for work"


class Miner(Robot):
    def __init__(self, name, battery=100, resource="stone", **kwargs):
        super().__init__(name=name, battery=battery, **kwargs)
        self.resource = resource
        self.state = "mine"

    def mine(self) -> str:
        return f"{self.name} mined {self.resource}"

    def status(self):
        return [self.name, self.battery, "mining", self.resource]


class Transporter(Robot):
    def __init__(self, name, battery=100, cargo=0, **kwargs):
        super().__init__(name=name, battery=battery, **kwargs)
        self.cargo = cargo
        self.state = "transporting"

    def transport(self) -> str:
        return f"{self.name} transported {self.cargo} kg"

    def status(self):
        return [self.name, self.battery, "transporting", self.cargo]


class Builder(Robot):
    def __init__(self, name, battery=100, material="brick", **kwargs):
        super().__init__(name=name, battery=battery, **kwargs)
        self.material = material

    def build(self):
        return f"{self.name} built a wall from {self.material}"

    def status(self):
        return [self.name, self.battery, "building", self.material]


class MinerTransporter(Miner, Transporter):
    def __init__(self, name, battery=100, resource="stone", cargo=0, **kwargs):
        super().__init__(
            name=name,
            battery=battery,
            resource=resource,
            cargo=cargo,
            **kwargs,
        )

    def work(self):
        mine = Miner.mine(self)
        transport = Transporter.transport(self)
        return f"{mine}\n{transport}"


class TransporterBuilder(Transporter, Builder):
    def __init__(self, name, battery=100, cargo=0, material="brick", **kwargs):
        super().__init__(
            name=name,
            battery=battery,
            cargo=cargo,
            material=material,
            **kwargs,
        )

    def work(self):
        transport = Transporter.transport(self)
        build = Builder.build(self)
        return f"{transport}\n{build}"


class SuperRobot(Builder, MinerTransporter):
    def __init__(
        self,
        name,
        battery=100,
        resource="stone",
        cargo=0,
        material="brick",
        **kwargs,
    ):
        super().__init__(
            name=name,
            battery=battery,
            resource=resource,
            cargo=cargo,
            material=material,
            **kwargs,
        )

    def work(self):
        mine = Miner.mine(self)
        transport = Transporter.transport(self)
        build = Builder.build(self)
        return f"{mine}\n{transport}\n{build}"
    


mt = MinerTransporter("Truck", 80, "ore", 500)
name, battery, mode, spec = mt.status()
print(f'Robot {name} has charge {battery}% and stay in {mode} mode with {spec}')
print(mt.work())
print()
tb = TransporterBuilder("Crane", 90, 300, "concrete")
name, battery, mode, spec = tb.status()
print(f'Robot {name} has charge {battery}% and stay in {mode} mode with {spec}')
print(tb.work())
print()
sr = SuperRobot("Megatron", 75, "titanium", 1000, "steel")
name, battery, mode, spec = sr.status()
print(f'Robot {name} has charge {battery}% and stay in {mode} mode with {spec}')
print(sr.work())