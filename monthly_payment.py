def calculate_monthly_payment(principal, annual_rate, years):
    # Räkna rate
    r = annual_rate / 100 / 12
    # beräkna months
    n = years * 12
    
    # Använd den givna formeln: A = (P * r(1+r)^n) / ((1 + r)^n - 1)
    A = (principal * r * (1 + r) ** n) / ((1 + r) ** n - 1)
    
    return A

principal = float(input("Lånebelopp: "))
annual_rate = float(input("Årsränta (%): "))
years = int(input("Löptid (år): ")) 
payment = calculate_monthly_payment(principal, annual_rate, years)

# Skriv ut resultatet
print(f"Din månatliga betalning är: {payment:.2f} kr")
