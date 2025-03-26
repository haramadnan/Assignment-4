def agreement_bot():
    print("🤖 Welcome to the Agreement Bot!")
    print("Before proceeding, you must agree to our terms and conditions.\n")

    # Agreement text
    agreement_text = """
    Terms & Conditions:
    1. You must be at least 18 years old to use this service.
    2. Your data may be stored for security purposes.
    3. Any misuse of this service is prohibited.
    4. We are not responsible for any loss or damage.
    """

    print(agreement_text)

    # Asking for user confirmation
    while True:
        user_response = input("Do you agree to the terms? (yes/no): ").strip().lower()
        if user_response == "yes":
            print("\n✅ Thank you! You have successfully agreed to the terms.")
            break
        elif user_response == "no":
            print("\n❌ You must agree to the terms to continue.")
        else:
            print("\n⚠ Invalid response. Please type 'yes' or 'no'.")

# Run the agreement bot
agreement_bot()