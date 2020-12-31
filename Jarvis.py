import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  
        

    speak("Sahil tu kutta hai Aur Parikshit Bhai app kaise hain , kafi din ho gya appse bat ni kiye          hey Sahil here is Todays Sports Headlines   India vs Australia A, 2nd Practice Match Day 3, Live Cricket Score: AUSA struggling, three down India vs Australia A (IND vs AUS) second Practice Live Cricket Score Online Updates: India declared their innings on 386/4 and set a massive target of 473 runs for the hosts to chase. By: Sports Desk | Updated: December 13, 2020 10:0:14 am india vs australia aIndia vs Australia A Practice Live Score: All to play for on the final day. (BCCI Photo) India vs Australia A second Practice Live Cricket Score: India’s Shubman Gill pushed his claims to make his debut in the opening test against Australia in Adelaide with a classy 65 in the warmup match as the touring side’s batsmen made merry against their injury-hit opponents on Saturday. Regular India opener Mayank Agarwal also spent time in the middle during his knock of 61 while Hanuma Vihari and Rishabh Pant made unbeaten centuries. After Australia’s all-rounder and test hopeful, Cameron Green was ruled out due to concussion on Friday, the local side also lost seamer Sean Abbott to injury as India moved on to 386 for four, extending their lead to 472 in the three-day match. LIVE BLOG India vs Australia A Live Score Updates: 13 DEC 2020 WICKET! Mohammed Siraj joins the attack for the visitors and he reaps rewards off the very first ball! He sends back Maddinson as he is caught out by fellow pacer Navdeep Saini. The batsman departs for 14. Alex Carey comes on next. AUSA: 29/3 (12 overs) 13 DEC 2020 SHAMI AGAIN! Shami is on a roll! He gets his second wicket of the day as he traps Joe Burns between the wickets. The opener's dismal afternoon comes to an end as he walks off for just 1. Maddinson smacks Bumrah for two fours in the next over. AUSA: 21/2 (10 overs) 13 DEC 2020 WICKET! GONE! Marcus Harris goes back to the pavilion early on in the innings as he is dismissed by Shami. The batsman tried to nick the ball behind for a four but he is caught by Prithvi Shaw. Harris departs on 5. Next up, Nic Maddinson. AUSA: 6/1 (4.1 overs) 13 DEC 2020 Harris, Burns begin the chase Marcus Harris and Joe Burns are at the crease at the start of the third day after India declared on 386/4. Mohammad Shami opens the attack for the visitors and he comes up with a maiden. Burns opens the hosts account in the next over. AUSA: 2/0 (2 overs) 13 DEC 2020 Hello and welcome! Hello and welcome to the live commentary of the warmup match between India and Australia before the start of the Test series on December 17. After Rishabh Pants final over blitzkrieg on the second day, India will look to build on the agony of the hosts. They will start the final day on 386/4 with a massive 472-run lead. Hanuma Vihari (104*) and Rishabh Pant (103*) are in the middle. Australia A Squad: Playing: Joe Burns, Marcus Harris, Nic Maddinson, Ben McDermott, Jack Wildermuth, Alex Carey (c & wk), Sean Abbott, Will Sutherland, Mitchell Swepson, Mark Steketee, Patrick Rowe, Harry Conway, Cameron Green India Squad: Playing: Prithvi Shaw, Mayank Agarwal, Shubman Gill, Hanuma Vihari, Ajinkya Rahane (c), Rishabh Pant (wk), Wriddhiman Saha, Navdeep Saini, Mohammed Shami, Mohammed Siraj, Jasprit Bumrah © IE Online Media Services Pvt Ltd TAGS:India Vs Australia What Happens To An Island Resort During A Pandemic The Better Traveller | Sponsored Coding Classes For Age 6-18 by IIT/ Harvard Alumnus Help us to help you take the informed decision by booking a free trial now! Laptop/Desktop is mandatory. CampK12 Sponsored OnePlus Nord open sales postponed to August 6 due to high pre-orders Business Line Sponsored Famous US Lottery Now in India golotter.com Sponsored Mohammed Siraj’s spirit of cricket wins hearts during India vs Australia A IndianExpress Watch: Jasprit Bumrah gets guard of honour for his maiden first-class 50 IndianExpress Buy Bitcoin (BTC) for as low as ₹10 on INSTA CoinDCX Sponsored AB De Villiers reacts to Virat Kohli’s scoop shot in Sydney IndianExpress India vs Australia A second Practice Match Live Cricket Score: Day 2 of pink ball tour match IndianExpress ₹12,000 Crore US Lottery Now Also Available in Indi Lotto Smile | Sponsored SUNDAY STORYXFarmers concern: Will lose land to corporates because of new lawsFarmers concern: Will lose land to corporates because of new laws ")       

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said:{query}\n")

    except Exception as e:
        print(e)    
        print("Say that again please...")  
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")   


        elif 'play music' in query:
            music_dir = 'D:\\Non Critical\\songs\\Favorite Songs2'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\Haris\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'email to Sahil' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "ss2035810@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend Sahil bhai. I am not able to send this email")    
