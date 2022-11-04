def generate_result(opA,opB,op,operator):

    if operator == "-":
        op.append(opA-opB)
    else:
        op.append(opA+opB)
 
def arithmetic_arranger(problems,val = False):
    
    try:
        
        assert len(problems) <= 5, 'ERROR -- Too many problems.\n'
        
        op1 = []
        op2 = []
        operat = []
        result = []
        
        st1 = str()
        st2 = str()
        st3 = str()
        
        for i in range(len(problems)):
            
            problem = problems[i].split()
            
            op1.append(problem[0])
            op2.append(problem[2])
            operat.append(problem[1])
            
            assert problem[0].isdigit() and problem[2].isdigit(), 'Error: Numbers must only contain digits.\n'
            assert len(problem[0]) <= 4 and len(problem[2]) <= 4, 'Error: Numbers cannot be more than four digits.\n'
            assert problem[1] in "+-", "Error: Operator must be '+' or '-'.\n"
            
            if val:
                
                if problem[1] == '+':

                    # print(f"{problem[0]:>6}\n+{problem[2]:>5}\n" + "_"*7) 
                    generate_result(int(problem[0]),int(problem[2]),result,'+')

                elif problem[1] == '-':

                    # print(f"{problem[0]:>6}\n-{problem[2]:>5}\n" + "_"*7)
                    generate_result(int(problem[0]),int(problem[2]),result,'-')
        
        for i in range(len(problems)):
            
            
            st1 += f"{op1[i]:>8}   "
            st2 += f"{operat[i]}{op2[i]:>7}   "
                
            if val:
                st3 += f"{result[i]:>8}   "
        
        print(st1)
        print(st2)
        print((("_"*8)+"   ")*len(problems))
        print(st3)
        
    except AssertionError as msg:
        print(msg)
        
operations = ["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49", "523 - 455"]
arithmetic_arranger(operations, True)