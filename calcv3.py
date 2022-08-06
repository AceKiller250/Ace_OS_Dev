while True:
    import sys
    from tqdm import tqdm
    import time
    import progressbar
    from time import sleep
    import os

    import os
    import sys
    import psutil
    import logging
    from subprocess import call


    pathname = os.path.dirname(sys.argv[0])



    foldername = os.path.abspath(pathname)
    foldername = foldername.replace(r'\test', r'\choose.py')
    print(foldername)

    def clear():
        # check and make call for specific operating system
        call('cls')

    def restart_program():
        """Restarts the current program, with file objects and descriptors
           cleanup
        """
        os.startfile(sys.argv[0])
        sys.exit()


    # Function to create
    def animated_marker():
        widgets = ['Checking if Operator Valid: ', progressbar.AnimatedMarker()]
        bar = progressbar.ProgressBar(widgets=widgets).start()

        for i in range(10):
            time.sleep(0.1)
            bar.update(i)


    # Driver's code


    #rich loading bar
    def richbar():
        import time

        from rich.progress import Progress

        with Progress(transient=True) as progress:

            task1 = progress.add_task("[purple]Processing...", total=300)

            while not progress.finished:
                progress.update(task1, advance=6.0)
                time.sleep(0.02)
    # animated_marker()

    ops = ("-", "+", "/", "*")

 

    while True:
        try:
            num1 = float(input("Enter First Number: "))
            print('The variable a number')
            break
        except:
            print('\n')

            print('Invalid Input (must be a NUMBER)')




    while True:
        try:
            print('\n')

            op = input("Enter operator (-, +, /, or *): ")
        except:
            print('\n')
            print("Invalid input")

        if op in ops:
            animated_marker()
            break
        else:
            animated_marker()
            print("IInvalid operator")


    try:
        print('\n')
        num2 = float(input(" Enter Second Number: "))
        tmp = int(num1)
        print('The variable a number')
    except ValueError:
        print('Invalid Input')


    #for i in tqdm(range(100),
    #              desc="Calculating...",
    #              ascii=False, ncols=75):
    #    time.sleep(0.01)

   

    if op == "+":
        print(num1 + num2)
    elif op == "-":
        print(num1 - num2)
    elif op == "/":
        print(num1 / num2)
    elif op == "*":
        print(num1 * num2)
    else:
        print("Invalid operator")

    richbar()
    print("Complete.")
    while True:
        # main program
        while True:
            answer = str(input('Run again? (y/n): '))
            if answer in ('y', 'n'):
                break
            print("invalid input.")
        if answer == 'y':
            print("Restarting Script...")
            break
        else:
            print("Script terminating...")
            choosepath = str(foldername)
            os.startfile(foldername)
            break
    
    sys.exit
        
    sleep(3)