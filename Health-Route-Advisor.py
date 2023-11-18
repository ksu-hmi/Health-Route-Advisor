def advice():
#introduction of program with brief explanation of urgent care, primary care, and emergency room visits
    print('Welcome to Health Route Advisor, please briefly review the information below before you begin.')
    print('\n\nPrimary Care is intended for non-urgent conditions that can wait for a scheduled appointment')
    print('\n\nUrgent Care is an additional resource for if you cannot obtain a timely primary care visit and are experiencing a mild, non-life threatening illness or injury')
    print('\n\nEmergency room visits are for severe illness or injury with the potential to be life-threatening. Also, for any life-threatening symptoms to include chest pain, facial droop with slurred speech or weakness/numbness, difficulty breathing, uncontrolled breathing.')
    print('*    *    *    *    *    *    *    *    *    *    *    *    *    *    *    *    *    ')
    
# Gather information about symptoms, begin with most severe
    emergency_room1 = input('Please answer yes "Y" or no "N".\nIf "YES" to any of the following symptoms, please call an ambulance or go to the emergency room immediately for evaluation.\n\nAre you experiencing chest pain, difficulty breathing, facial droop, weakness/numbness on one side, loss of vision, loss of consciousness, head injury, seizure, uncontrolled bleeding?')
    if emergency_room1.lower() == "y":
        print("Please call an ambulance or seek immediate care from emergency room.\nThank you for using the Health Route Advisor and get well soon!")
    elif emergency_room1.lower() == "n":
        emergency_room2 = input('Please answer yes "Y" or no "N".\nIf "YES" to any of the following, please go to the emergency room\n\nAre you experiencing severe dizziness, suspected broken bone or dislocation, burn with blister, severe abdominal pain, large cut that may need stitches, fever >103 F, fever with rash, vaginal bleeding while pregnant, suspected poisoning, mental health crisis?')
        if emergency_room2.lower() == "y":
            print('Please seek care at an emergency room.')
        else:
            fever = input("Do you have a mild fever without rash? (Y/N): ")
            wheeze = input("Are you wheezing or slightly short of breath? (Y/N): ")
            cut_small = input("Do you have a small cut or minor injury? (Y/N): ")
            flu = input("Do you have symptoms of cold or flu? (Y/N): ")
            vomiting = input("Are you experiencing nausea with vomiting? (Y/N): ")
            diarrhea = input("Are you experiencing diarrhea? (Y/N): ")
            urine = input("Are you having pain or difficulty with urinating? (Y/N): ")
            bite = input("Do you a minor animal or insect bite? (Y/N): ")
            allergy = input("Are you experiencing mild symptoms of allergic reaction(redness, itching, swelling, no difficulty breathing)? (Y/N): ")
            if fever or wheeze or cut_small or flu or vomiting or diarrhea or urine or bite or allergy == "y":
                print("Please seek treatment at an urgent care. Thank you for using Health Route Advisor. Get well soon!")
