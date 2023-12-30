label exPhoneMenu:
    $ renpy.dynamic('apps', 'appHome', 'contacts', 'msgList', 'mom', 'phone', 'sis')
    $ appHome = AppHome()
    $ apps = []
    $ apps.append(AppContacts())
    $ apps.append(AppMsgList())
    $ apps.append(AppMsgDx())
    $ contacts = {}
    $ phone = Phone(appHome, apps, contacts)
    $ mom = phone.addContact("Mom")
    $ sis = phone.addContact("Sis")
    $ me = phone.addContactOwner("Me")
    scene bg village
    show screen phoneButtonScr(phone)
    "Tum-ti-tum"
    menu (phone, screen="phoneChoiceScr"):
        "What to do? I could text my sister."
        "Nothing":
            pause 1.0
            "You twiddle your thumbs."
        ".phone":
            "I did a phone thing."
        ".phone.msg.Sis":
            call .sis
    "Done."
    $ phone.close()
    hide screen phoneButtonScr
    pause 0.5
    scene black
    return

label .sis:
    $ renpy.dynamic('pc', 'sis')
    $ phone.changeMenuMode()
    $ pc = phone.msgCharTx("Sis")
    $ sis = phone.msgCharRx("Sis")
    window hide
    pause 1.0
    pc "Hi sis. What's up?"
    #$ pc("Hi sis. What's up?")
    pause 1.0
    $ sis("Nothing. You?")
    pause 1.0
    #sis "Nothing. You?"
    #$ sis.smsReply("Hi sis. What's up?")
    #"I wonder if she will reply?"
    #pause
    #$ sis.sms("Nothing. You?")
    #pause
    return