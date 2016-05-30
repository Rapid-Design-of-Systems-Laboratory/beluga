Steps to solving a problem

- Start with "Problem" object
- Perform series of steps to create Necessary conditions
- Another series of steps to create BVP (solver-specific?)
- Series of steps to solve (using continuation + solver etc.) and make "solution" object

Strategy class
    - __call__ method that calls relevant methods in other classes?
    - Array of "action" objects with __call__ methods in them
        - Process quantities
        - Make costates
        - Make costate rates

        - Process constraints ... etc.?
    - Command object can also be iterable (for continuation?)
    - Action object operates on problem??

Calculus class?
    - Take derivative using chain rule
