import function_rat_num as fr 
import type_num as ty
import function_comp_num as fc


type = ty.type()

while type =='rational':
    fr.main_terminal()


     
if type == 'complex':
    repeat = True
    while repeat == True:
        operands = fc.insert_numbers()
        if operands[2] == "+":
            fc.rec_in_file(fc.addition(fc.take_rational_part(operands[0]), fc.take_symbol(operands[0]), fc.take_imaginary_part(operands[0]), fc.take_rational_part(operands[1]), fc.take_symbol(operands[1]), fc.take_imaginary_part(operands[1])))
        elif operands[2] == "-":
            fc.rec_in_file(fc.deduction(fc.take_rational_part(operands[0]), fc.take_symbol(operands[0]), fc.take_imaginary_part(operands[0]), fc.take_rational_part(operands[1]), fc.take_symbol(operands[1]), fc.take_imaginary_part(operands[1])))
        elif operands[2] == "*":
            fc.rec_in_file(fc.mult(fc.take_rational_part(operands[0]),  fc.take_symbol(operands[0]), fc.take_imaginary_part(operands[0]), fc.take_rational_part(operands[1]), fc.take_symbol(operands[1]), fc.take_imaginary_part(operands[1])))
        else:
            fc.rec_in_file(fc.division(fc.take_rational_part(operands[0]),  fc.take_symbol(operands[0]), fc.take_imaginary_part(operands[0]), fc.take_rational_part(operands[1]), fc.take_symbol(operands[1]), fc.take_imaginary_part(operands[1])))
        repeat = fc.repeat_or_no()