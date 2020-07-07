from packages import calculator

if __name__ == "__main__":
    root = calculator.Tk()
    calculator = calculator.Calculator(root)
    root.title('Calculator')
    root.mainloop()
