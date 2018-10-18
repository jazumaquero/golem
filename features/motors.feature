Feature: control differential motor using velocity tuple in X and Y axis

  Scenario: velocity in X is 0 and velocity in Y is 0 mean motors stopped
    Given vx equal 0
    And vy equal 0
    When do robot movement
    Then robot is stopped

  Scenario: velocity in X is 0 and velocity in Y is > 0 mean motors go forward
    Given vx equal 0
    And vy equal 1
    When do robot movement
    Then robot moves forward with speed 1 and curve left 0 and curve right 0

  Scenario: velocity in X is 0 and velocity in Y is < 0 mean motors go backward
    Given vx equal 0
    And vy equal -1
    When do robot movement
    Then robot moves backward with speed 1 and curve left 0 and curve right 0

  Scenario: velocity in X is > 0 and velocity in Y is  0 mean motors turn right
    Given vx equal 1
    And vy equal 0
    When do robot movement
    Then robot moves right with speed 1

  Scenario: velocity in X is < 0 and velocity in Y is  0 mean motors turn left
    Given vx equal -1
    And vy equal 0
    When do robot movement
    Then robot moves left with speed 1

  Scenario: velocity in X is > 0 and velocity in Y is > 0 mean motors go forward and slightly turn right
    Given vx equal 0.1
    And vy equal 1
    When do robot movement
    Then robot moves forward with speed 1 and curve left 0 and curve right 0.1

  Scenario: velocity in X is < 0 and velocity in Y is > 0 mean motors go forward and slightly turn left
    Given vx equal -0.1
    And vy equal 1
    When do robot movement
    Then robot moves forward with speed 1 and curve left 0.1 and curve right 0

  Scenario: velocity in X is > 0 and velocity in Y is > 0 mean motors go backward and slightly turn right
    Given vx equal 0.1
    And vy equal -1
    When do robot movement
    Then robot moves backward with speed 1 and curve left 0 and curve right 0.1

  Scenario: velocity in X is < 0 and velocity in Y is > 0 mean motors go backward and slightly turn left
    Given vx equal -0.1
    And vy equal -1
    When do robot movement
    Then robot moves backward with speed 1 and curve left 0.1 and curve right 0