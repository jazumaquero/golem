Feature: control differential motor using velocity tuple in X and Y axis

  Scenario: velocity in X is 0 and velocity in Y is 0 mean motors stopped
    Given vx equal "0"
    And vy equal "0"
    When do robot movement
    Then robot is stopped

  Scenario: velocity in X is 0 and velocity in Y is > 0 mean motors go forward
    Given vx equal "0"
    And vy equal "1"
    When do robot movement
    Then robot moves "FORWARD" with speed "1" and curve left "0" and curve right "0"

  Scenario: velocity in X is 0 and velocity in Y is < 0 mean motors go backward
    Given vx equal "0"
    And vy equal "1"
    When do robot movement
    Then robot moves "BACKWARD" with speed "1" and curve left "0" and curve right "0"

  Scenario: velocity in X is > 0 and velocity in Y is  0 mean motors turn right
    Given vx equal "0"
    And vy equal "1"
    When do robot movement
    Then robot moves "RIGHT" with speed "1"

  Scenario: velocity in X is < 0 and velocity in Y is  0 mean motors turn left
    Given vx equal "0"
    And vy equal "1"
    When do robot movement
    Then robot moves "LEFT" with speed "1"
