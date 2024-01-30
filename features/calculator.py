import wolframalpha

def WolfRamAplpha(command):
    apikey = "8Q76UJ-LYPVXAY83X"
    request = wolframalpha.Client(apikey)
    re = request.query(command)

    try:
        answer = next(re.results).text
        return  answer
    except:
        print("the value is not answerable")

def Calc(command):
    problem = command.replace("calculate ", "")
    Term = str(problem)
    Final = str(Term)

    try:
        result = WolfRamAplpha(Final)
        if '/' in result:
            # Split the result into numerator and denominator
            parts = result.split('/')
            numerator = float(parts[0].strip())
            denominator = float(parts[1].split()[0].strip())  # Extract numerical part before any additional text
            decimal_result = numerator / denominator
            
            return f"{numerator}/{denominator} is approximately {decimal_result:.2f}"
        else:
            return problem + " is " + result
    except:
        print("An error occurred while processing the request")







