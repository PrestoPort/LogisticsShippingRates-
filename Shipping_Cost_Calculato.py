#Shipping Cost Calculator

## Input package weight and Shipping rate
weight = float (input("Enter the package weight in kilograms:"))
rate = float (input("Enter the shipping rate per kilograms:"))

## Calculate shipping cost
shipping_cost = weight * rate
## Display the result
print(f"Shipping Cost: {shipping_cost} USD")
