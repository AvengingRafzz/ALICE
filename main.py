# Main File. Run ALICE from here

# Import necessary modules
import ai_bot
import ai_speak
import ai_listen
import ai_welcome
import calculate
import date_time
import games
import image_capture
import internet_speed
import open_apps
import login
import signup
import translator
import weather

if __name__ == "__main__":
    try:
        # Get user choice for login or sign up
        choice = int(input("1. Login\n2. Sign Up\n"))

        # Perform action based on user choice
        if choice == 1:
            login_result = login.login()

            if login_result is True:
                # Display welcome message
                wish = ai_welcome.wish_me()
                print(wish)
                ai_speak.speak(wish)

                while True:
                    # Ask user to choose input method (text or microphone)
                    choice = int(input("1. Use Text\n2. Use Microphone\n"))

                    if choice == 1:
                        # Get user input from text
                        query = input("Rafan: ")
                        query = query.lower()

                        # Perform actions based on user input
                        if "weather" in query or "temperature" in query or "climate" in query:
                            weather.get_weather("52e874f99f88a68005c1078f7250ae2d", "Mumbai")
                        elif "date" in query:
                            date_time.current_date()
                        elif "time" in query:
                            date_time.current_time()
                        elif "open" in query:
                            open_apps.start(query)
                        elif "calculate" in query:
                            query = query.replace("calculate", "")
                            calculate.calc(query)
                        elif "internet speed" in query:
                            internet_speed.perform_speedtest()
                        elif "game" in query:
                            choice = int(input("1. Rock Paper Scissor\n2. Number Guessing Game\n3. Hangman\n"))
                            if choice == 1:
                                games.play_rps()
                            elif choice == 2:
                                games.play_ngg()
                            elif choice == 3:
                                games.play_hangman()
                            else:
                                print("Invalid choice")
                                ai_speak.speak("Invalid choice")
                        elif "screenshot" in query or "screen" in query:
                            image_capture.screenshot()
                        elif "camera" in query or "photo" in query:
                            image_capture.camera()
                        elif "translate" in query:
                            query = query.replace("translate", "")
                            translated_text = translator.translate(query)
                            print(translated_text)
                            ai_speak.speak(translated_text)
                        else:
                            answer = ai_bot.ai_output(query)

                            if answer is False:
                                bye = "Bye, hope to see you soon"
                                print(f"AI Response: {bye}")
                                ai_speak.speak(bye)
                                break
                            else:
                                print(f"AI Response: {answer}")
                                ai_speak.speak(answer)

                    elif choice == 2:
                        # Get user input from microphone
                        query = ai_listen.listen()

                        # Perform actions based on user input
                        if "weather" in query or "temperature" in query or "climate" in query:
                            weather.get_weather("52e874f99f88a68005c1078f7250ae2d", "Mumbai")
                        elif "date" in query:
                            date_time.current_date()
                        elif "time" in query:
                            date_time.current_time()
                        elif "open" in query:
                            open_apps.start(query)
                        elif "calculate" in query or "+" in query or "-" in query or "*" in query or "/" in query:
                            query = query.replace("calculate", "")
                            query = query.replace("jarvis", "")
                            calculate.calc(query)
                        elif "internet speed" in query:
                            internet_speed.perform_speedtest()
                        elif "game" in query:
                            choice = int(input("1. Rock Paper Scissor\n2. Number Guessing Game\n3. Hangman\n"))
                            if choice == 1:
                                games.play_rps()
                            elif choice == 2:
                                games.play_ngg()
                            elif choice == 3:
                                games.play_hangman()
                            else:
                                print("Invalid choice")
                                ai_speak.speak("Invalid choice")
                        elif "screenshot" in query or "screen" in query:
                            image_capture.screenshot()
                        elif "camera" in query or "photo" in query:
                            image_capture.camera()
                        else:
                            answer = ai_bot.ai_output(query)

                            if answer is False:
                                bye = "Bye, hope to see you soon"
                                print(f"AI Response: {bye}")
                                ai_speak.speak(bye)
                                break
                            else:
                                print(f"AI Response: {answer}")
                                ai_speak.speak(answer)

            elif login_result is False:
                incorrect = "Incorrect user credentials. Please try again"
                print(f"AI Response: {incorrect}")
                ai_speak.speak(incorrect)
        elif choice == 2:
            signup.sign_up()
    except Exception as e:
        print(e)
