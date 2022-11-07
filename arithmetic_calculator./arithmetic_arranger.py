def generate_result(opA,opB,operator):

    if operator == "-":
        return opA-opB
    else:
        return opA+opB

def arithmetic_arranger(problems,val = False):
    
    # Validating and initiating data
    if len(problems) > 5:
        return "Error: Too many problems."
    
    op1 = []
    op2 = []
    operator = []
    flag1 = False
    flag2 = False
    flag3 = False
    
    for problem in problems:
        p1, opr, p2 = problem.split()
        
        if not p1.isdigit() or not p2.isdigit():
            flag1 = True
            break
        
        if len(p1) > 4 or len(p2) > 4:
            flag2 = True
            break
        
        if opr not in "+-":
            flag3 = True
            break
        
        op1.append(p1)
        op2.append(p2)
        operator.append(opr)
    
    # Doing this as using a return inside a for loop might be harmful in other programming languages
    
    if flag1:
        return "Error: Numbers must only contain digits."
    
    if flag2:
        return "Error: Numbers cannot be more than four digits."
    
    if flag3:
        return "Error: Operator must be '+' or '-'."
    
    
    # Setting up the print
    biggest = []
    lines = []
    
    for i in range(len(operator)):
    
        biggest.append(max(len(op2[i]),len(op1[i]))+2)    
        lines.append("-" * biggest[i])
    
    st1 = ""
    st2 = ""
    st3 = ""
    
    # The if is necessary to pass the test :(
    for i in range(len(operator)):
        
        if i != len(operator)-1:
           st1 += f"{op1[i]:>{biggest[i]}}    "
           st2 += f"{operator[i]}{op2[i]:>{biggest[i]-1}}    "
           st3 += f"{lines[i]}    "
           
        else:
            st1 += f"{op1[i]:>{biggest[i]}}"
            st2 += f"{operator[i]}{op2[i]:>{biggest[i]-1}}"
            st3 += f"{lines[i]}"

    if val:
        
        results = []
        val_str = ""
            
        for i in range(len(operator)):
            results.append(generate_result(int(op1[i]),int(op2[i]),operator[i]))
        
        for i in range(len(results)):
            
            if i != len(results)-1:
                val_str += f"{results[i]:>{biggest[i]}}    "
            else:
                val_str += f"{results[i]:>{biggest[i]}}"
                
        return st1 + "\n" + st2 + "\n" + st3 + "\n" + val_str
    
    else:
        
        return st1 + "\n" + st2 + "\n" + st3