# SDET Challenge
This is a challenge to find a fake gold brink in a mix of 9. My algorith was:
1. To split the bricks into two groups of four with  one brick out on its own.
2. Then I would then weigh the two groups. 
3. If they both weigh the same, then I know that the one brick that was left out is the fake brick. 
4. If I have a lighter side on the scale, I then split that group evenely again and repeat
5. Then I get to two final bricks to weigh against each other. 
6. Finally I click on the number of the lightest brick


# Installation
## Prerequisets
- Have Cypress 3.11.9 installed (https://www.python.org/downloads/release/python-3119/)

## Steps to Install
1. Clone repo (if not already)
2. Install packages
    ```bash
    pip install -r requirements.txt 
    ```
3. Depending on your IDE, you may need to configure your test runner. 
    - On VS Code, you can open the command pallet and search for "Python:Configure Tests"
    - Then select pytest
    - Then click ". Root Directory"

4. Run the test in your IDE!!!
    - If you would like to run from command line, you can just run the following command:
        ```bash
        pytest
        ```



