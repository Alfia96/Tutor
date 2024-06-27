# Midterm Task III from HW 3 Task 3ia - Madelyn Bennett

# Get input file from user
input_file_name = input("Hello! Please enter the name of your input file:")

# Read file contents & print content - iterative process
input_file = open(input_file_name)
input_file_contents=input_file.read()
input_file.close()

sequence = input_file_contents

#Calculate sequence length
length = len(sequence)

# Get G and C count
g_c_count = sequence.count("G") + sequence.count("C")

# Get percent GC count
percent_g_c = (g_c_count*100.0) / length

# Get melting temp with equation from HW 3 Task ia
melting_temp = 81.5 + 0.41*(percent_g_c) - (500.0/length)

print("User's melting temp: " + str(melting_temp))

# Calculate reverse sequence
reverse_sequence = sequence[::-1]

#Calculate complement of reverse sequence
reverse_sequence_complement = reverse_sequence.replace("G","c")
reverse_sequence_complement = reverse_sequence_complement.replace("A","t")
reverse_sequence_complement = reverse_sequence_complement.replace("C","g")
reverse_sequence_complement = reverse_sequence_complement.replace("T","a")
reverse_sequence_complement = reverse_sequence_complement.upper()

print("User's reverse sequence complement: " + reverse_sequence_complement)

# Calculate probabilities of each nucleotide
# Probability is count of nucleotide / length of sequence
count_G = sequence.count("G")
count_C = sequence.count("C")
count_A = sequence.count("A")
count_T = sequence.count("T")

probability_G = count_G / length
probability_C = count_C / length
probability_A = count_A / length
probability_T = count_T / length

# Get user ouput_file_name
output_file_name = input("Please enter the name of the output file you want me to make: ")
output_file = open(output_file_name, "w")

# Make contents of output file for the user based on their input sequence
output_file_contents = "i. Input Sequence: " + sequence + " , Reverse Complement Sequence: " + reverse_sequence_complement + "\n"
output_file_contents += "ii. Nucleotide Probabilities: G: " + str(probability_G) + ", C: " + str(probability_C) + ", A: " + str(probability_A) + ", T: " + str(probability_T) + "\n"
output_file_contents += "iii. %GC Contents: " + str(percent_g_c) + "%, Melting Temperature in C: " + str(melting_temp) + " Degrees Celcius"

# Write the contents to their output file
output_file.write(output_file_contents)
output_file.close()

print("Wrote sequence information to: " + output_file_name)
