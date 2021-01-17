## Robot Navigation

A work on python assignment

### How to run

Please find in examples folder.

### Code package

The package structure:
```
.
├── LICENSE
├── README.md
├── environment.yml
├── examples
│   ├── input.txt
│   ├── run_robot_arg.py
│   └── run_robot_cfg.py
├── inputs
│   ├── test_0
│   │   ├── input_0.txt
│   │   └── user_config.yml
│   └── test_1
│       ├── input_0.txt
│       └── user_config.yml
├── setup.py
├── src
│   └── robotnavigation
│       ├── action.py
│       ├── board.py
│       ├── command.py
│       ├── direction.py
│       ├── entity.py
│       └── utils.py
└── tests
    ├── fixtures
    │   ├── input.txt
    │   ├── invalid_env
    │   │   ├── invalid_input.txt
    │   │   └── user_config.yml
    │   └── sample_env
    │       ├── sample_input.txt
    │       └── user_config.yml
    ├── test_agent.py
    ├── test_env.py
    └── test_parser.py
```

### Inputs

There are two kinds of input:

1. From config folder:

The inputs are placed in "Input" folder, where each subfolder represents for a single testcase including two files:

- Yaml file for environment config and pointer to test case file url.
- Test case for robot movement.
  
Please find in *examples/run_robot_cfg.py*

2. From arguments setup:

Simply enter arguments as Dictionary, please find in *examples/run_robot_arg.py*

### Code explanation

- Board: set up environment including board size (X, Y) and init robot/agent
- Entity: for agent/robot class
- Command: for command processing, parse command from input file
- Action, Direction: definitions for Action [PLACE, MOVE, LEFT, RIGHT, REPORT], Direction[NORTH, SOUTH, EAST, WEST]
- Utils: includes some functions for loading environments

### Tests

Please find in "tests" folder with pytest applied.

