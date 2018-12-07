Feature: control differential motor using velocity tuple in X and Y axis

  @robot
  Scenario Outline: Robot moves with given velocity X and Y
    Given robot vx equal <vx>
      And robot vy equal <vy>
    When do robot movement
    Then robot direction <direction>
      And robot speed is <speed>
      And robot curve left is <curve_left>
      And robot curve right is <curve_right>

  Examples: Robot state depending on vx and vy
    | vx   | vy | direction | speed | curve_left | curve_right |
    | 0    | 0  | STOP      | -     | -          | -           |
    | 0    | 1  | FORWARD   | 1     | 0          | 0           |
    | 0    | -1 | BACKWARD  | 1     | 0          | 0           |
    | 1    | 0  | RIGHT     | 1     | -          | -           |
    | -1   | 0  | LEFT      | 1     | -          | -           |
    | 0.1  | 1  | FORWARD   | 1     | 0          | 0.1         |
    | -0.1 | 1  | FORWARD   | 1     | 0.1        | 0           |
    | 0.1  | -1 | BACKWARD  | 1     | 0          | 0.1         |
    | -0.1 | -1 | BACKWARD  | 1     | 0.1        | 0           |
