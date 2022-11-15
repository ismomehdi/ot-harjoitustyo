```mermaid
sequenceDiagram
  main->>Machine: Machine()
  Machine->>Machine._tank: self._tank = FuelTank()
  Machine->>Machine._tank: self._tank.fill(40)
  Machine->>self._engine: self._engine = Engine(self._tank)
  
  
  main->>Machine: Machine.drive()
  Machine->>self._engine: self._engine.start()
  Machine->>Machine.running: running = self._engine.is_running()
  self._engine->>Machine.running: self._fuel_tank.fuel_contents > 0
  
  alt if running
        Machine->>self._engine: self._engine.use_energy()
        self._engine->>Machine._tank:self._fuel_tank.consume(10)
  end

