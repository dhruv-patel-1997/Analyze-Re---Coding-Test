import sys

threshold=float(sys.argv[1])
limit=float(sys.argv[2])

# Input validation
if threshold<0.0 or threshold>1000000000.0 or limit<0.0 or limit>1000000000.0:
	print("Threshold or limit value must be between 0 and 10,000,000")
	exit()

# Take number of input to be entered by user.
user_inputs=int(input("Please enter number of input you wish to provide: "))

# Input validation
if user_inputs>100:
	print("Maximum value of input is 100.")
	user_inputs=100


output=[] # Contains the output array
sum=0 # Sum of all the output number

print("\nInput: ")
# For loop to take values from user and append to output accordingly
for y in range(user_inputs):
  x=float(input())
  # Input validation
  if(x>10000000.0):
  	print("Please enter the input vales between 0 and 10,000,000")
  	exit()
  # Append 0 to output
  if x<=threshold:
    output.append(float(0))
  else:
    if(sum+(x-threshold)<=limit):
        output.append(float(x-threshold))
    else:
        output.append(float(limit-sum))
    sum+=output[-1]


output.append(sum)
print("\n")
print("Output: ")

# Print the output array
for o in output:
	print(o)
