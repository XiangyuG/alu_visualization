import re
import sys

if (len(sys.argv) != 2):
  print("")
  sys.exit(1)

opcode = int(sys.argv[1])

res = ["!=","<",">","=="] 

print("bit sampling_equivalent_0_pred_raw_2_1_stateful_alu_1_0_rel_op_0(int operand1, int operand2, int opcode) {")
print("return operand1" + res[opcode] + "operand2;")
print("}\n")
