from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os




def setup():
    chatbot = ChatBot('Bot',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    trainer='chatterbot.trainers.ListTrainer')
    #for file in os.listdir('C:/Users/aman/chatbot/english/'):
       #convData = open(r'C:/Users/aman/chatbot/english/' + file,encoding='latin-1').readlines()
        #chatbot.set_trainer(ListTrainer)
        #chatbot.train(convData)
        #print("Training completed")
    
    return chatbot

bot1 = setup()

bot1.train([
"""What is Road Side Assistance (RSA)
""",

"""
Road Side Assistance is a service that provides you with the necessary help in case you are stranded on the road when your car breaks down. For example, breakdown cover may include jump starting an automobile, towing a vehicle, helping to change a flat tyre, providing a small amount of fuel when a vehicle runs out of it, or helping people who are locked out of their cars, etc.

""",

" Hi ",
" Hii, How can I help you? ",
"hello",
" Hii, How can I help you?",
"How are you",
"I am fine thank you:), How can I help you?",




])





bot1.train([
"""Which are the services provided by ICICI Lombard under Road Side Assistance (RSA)
""",

""" *
• Breakdown support over phone
• Minor Repairs
• Flat Tyre 
• Battery jump start
• Arrangement of keys
• Towing on breakdown/accident
• Arrangement of rental vehicle
• Arrangement/ Supply of fuel
• Arrangement of Accommodation
• Message Relay

Note: For details kindly refer Policy wordings from Web site for private car package policy.
*For list of services applicable in a policy, please refer policy schedule.

""",
])
bot1.train([
"""What is meaning of insurance
""",

"""
Insurance is a protection against the financial loss arising on the happening of an unexpected event. A person can avail this protection by paying a premium to an insurance company.

""",
])
bot1.train([
"""What is the period of General Insurance policies
""",

"""
Typically, General Insurance contracts are for a one-year period only.

""",
])
bot1.train([
"""What are the benefits of buying Motor Insurance online
""",

"""
When you buy Motor Insurance online, you get an instant policy, as there is no documentation or paperwork involved. In addition, you have the advantage of choosing from multiple payment options e.g. Credit Card (Visa, Master Amex card), Net banking, Debit Card etc.

""",
])
bot1.train([
"""What are the various types of vehicle that I can insure online
""",

"""
Currently only Private Car and Two-wheeler can be insured online.

""",
])
bot1.train([
"""Why do I need to insure my vehicle
""",

"""
Your vehicle is probably one of the most expensive things you own. Insurance protects this asset and helps you cope with the financial loss caused by accidents, damage or theft. Another reason is that while driving, you are responsible for the safety of:
• Your passengers
• Your fellow drivers
• Other people's property
• Pedestrians
• Yourself
Insurance helps cover the costs of potential damages or injuries in case of an unforeseen accident or theft. Above all, in India it is mandatory to have at least a Third Party Motor Insurance before you can drive on the roads.

""",
])
bot1.train([

"""What is No Claim Bonus (NCB)
""",

"""
No Claim Bonus (NCB) is a discount on premium of the Own Damage (OD) portion of your vehicle when you renew your policy, provided you have not made any claim during the last policy period. The NCB can be accumulated up to a maximum limit of 50% on OD premium.

You can transfer the full benefits of NCB, even when you shift your motor insurance to ICICI Lombard from any other Insurance company.

NCB benefits are given as per the below :

$$ All Type Of Vehicles	--	% Of Discount On Own Damage Premium
No claim made or pending during the preceding full year of insurance	--	20%
No claim made or pending during the preceding 2 consecutive years of insurance	--	25%
No claim made or pending during the preceding 3 consecutive years of insurance	--	35%
No claim made or pending during the preceding 4 consecutive years of insurance	--	45%
No claim made or pending during the preceding 5 consecutive years of insurance	--	50%

""",
])
bot1.train([

"""Is my No Claim Bonus (NCB) transferable
""",

"""
Yes, in case you are the customer of ICICI Lombard, or are switching/changing to ICICI Lombard from any other insurance company, and have accrued some NCB from your previous insurer, you can get the same transferred provided the vehicle is insured within 90 days of your renewal due date. The same applies if you switch/change from ICICI Lombard to other insurance company

""",
])
bot1.train([
"""What is the rate at which NCB is transferred from my previous insurance company to ICICI Lombard
""",

"""
The NCB will be transferred to ICICI Lombard motor policy at the same rate that you are entitled to get from the previous insurance company on renewal of your policy. The NCB will be available, provided you show evidence that you are entitled to No Claim Bonus from your previous insurance company. Evidence can be in form of:

• A renewal notice or
• A letter confirming the NCB entitlement from the previous insurer or
• A written declaration (kindly note that in case of a false declaration, the policy will be subject to cancellation)

Click here to view the wordings of the written declaration

""",
])
bot1.train([

"""Can I renew my Two-wheeler insurance policy online
""",

"""
yes, you can renew your Two-wheeler insurance policy online, starting 60 days before the expiry of your existing policy.

""",
])
bot1.train([
"""What is the penalty that I may have to incur in case my two-wheeler is uninsured
""",

"""
As per section 197 of motor vehicle act 1988, driving without insurance will lead to a fine of up to ` 1000 or imprisonment for up to 3 months or both.

""",
])
bot1.train([

"""Is it mandatory to insure my Two-wheeler as per law
""",

"""
Under the Motor Vehicle Act, third party insurance is mandatory for every vehicle on the road. Third Party Liability covers:
• Legal liability due to permanent injury and/or death of a third party
• Legal liability due to damage to a third party’s property

""",
])
bot1.train([
"""What is Long Term Two-wheeler Insurance (LTTW)
""",

"""
The Insurance Regulatory and Development Authority of India (IRDAI) has introduced a long-term insurance policy for two wheelers.
This means that you don’t have to renew your policy every year. Instead, you can opt for an insurance policy that is valid for three years. What’s more, by opting for long term insurance, you are immune to the revision of Third Party Rates every year, resulting in significant savings.

""",
])
bot1.train([
"""What are the benefits of a Long Term Two-wheeler Insurance
""",

"""
There are varied benefits available to you if you are opting for a Long Term Two Wheeler Policy (LT) as opposed to a one year policy:


One Year Policy	Long Term Policy
Single Policy certificate valid for 1 year only	Single Policy certificate valid for 3 years
Reminder for renewal every year	No worries or renewal reminder for 3 years
No ‘No Claim Bonus’ (NCB) benefits even if 1 claim is made in policy period	NCB will be applicable for 1 or more claims as per the policy period
Premium hike every year due to regulatory changes	Zero impact of hike in premium due to regulatory changes

""",
])
bot1.train([
"""Which documents will I require to transfer my NCB
""",

"""
A No Claim Bonus can be availed, provided you show evidence that you are entitled to a No Claim Bonus from your previous insurance company. Evidence can be in the form of:

A renewal notice or

A letter confirming the NCB entitlement from the previous insurer or

A written declaration (kindly note that in case of a false declaration, the policy will be subject to cancellation)
""",
])
bot1.train([ 
	"""What is a No Claim Bonus (NCB) """,

"""
NCB is a reward for not raising a claim. It is a discount on the premium of the Own Damage (OD) portion of your vehicle when you renew your policy, provided you have not made any claim during the last policy period of one year. The NCB can be accumulated up to a maximum limit of 50% on OD premium.
As for Long Term Two Wheeler Policy holders, the below would apply: ***********************************************

$$-- No Claim Bonus (NCB) Benefits for 3 Years.

$$--  No Claim During Policy Tenure - 40% NCB.

$$--  One Claim During Policy Tenure - 30% NCB.

$$--  Two Claims During Policy Tenure - 20% NCB.

""",
])

bot1.train([

"""What is Compulsory and Voluntary deductible """,

"""
Compulsory deductible means the amount that you will bear in case of a claim. Two-wheeler Insurance policies carry a Compulsory Deductible of ` 100.
Voluntary deductible is the amount you opt for as a higher deductible over and above the compulsive deductible in the event of the claim. (Final Claim amount will be after deduction of depreciation on parts, VD and compulsory deductible as per IMT)

""",
])

bot1.train([
"""What are the events covered in ICICI Lombard Motor Insurance policy
""",

"""
The ICICI Lombard Motor Insurance policy is a comprehensive vehicle insurance cover, which offers you:

• Any Loss or damage to your vehicle
• Third Party Liability
• Any permanent injury / death to a person caused by your insured vehicle
• Any damage caused to the property other than property belonging to the insured or held in trust or in custody or control of insured by your vehicle
• A Personal Accident Cover for the owner-driver of the vehicle while he is driving

In case of loss or damage to the vehicle or the accessories insured, the Company covers the insured if the accident occurs due to the following hazards:

• Fire, explosion, self ignition or lightning
• Burglary, housebreaking or theft
• Riot and strike
• Earthquake (fire and shock damage)
• Flood, typhoon, hurricane, storm, tempest, inundation, cyclone, hailstorm, frost
• Accident by external means
• Malicious act
• Terrorist activity
• Whilst in transit by road, rail, inland-waterway, lift, elevator or air
• Landslide and rockslide


""",
])
bot1.train([
"""What are the types of events or losses not covered under this policy
""",

"""
The following events or losses are not covered in this policy:
• Mechanical/ Electrical breakdown
• Wear and tear, ageing of vehicle
• Consequential loss*
• Depreciation
• Deliberate accidental loss
• Intoxicated driving
• Any contractual liability
• Damage to/ by a person driving any vehicles or cars without a valid license

* Consequential loss is an indirect loss, which is not directly resulting out of a loss event, but arising as a consequence of loss event. For example, Mr. Singh was on his way to office for an important meeting with client. Unfortunately, his vehicle met with a road accident resulting in damages to vehicle and it consumed lot of his time. Due to this, he could not attend the meeting resulting in loss of approx `15 Lakhs. Damages to vehicle due to the accident are covered however, but the loss of `15 Lakhs is consequential and hence not covered.

For details, kindly refer to the Two-wheeler Policy Wordings.

""",
])
bot1.train([
"""What is Third Party Liability cover
 Is it covered
""",

"""
Third Party Liability insurance covers losses to a third person who is not a party to the insurance contract. The Motor Third Party insurance covers the following losses:

• Any permanent injury / death to a person caused by your insured vehicle
• Any damage caused to the property (excluding vehicle) of some other individual by your insured vehicle

Liability is covered for an unlimited amount in respect of death or injury. Any damage to third party property is covered up to `7.5 Lakhs in case of Private Car and `1 Lakh in case of Two-wheeler.
""",
])
bot1.train([
"""What is Personal Accident Insurance cover
""",

"""
Personal Accident Insurance covers death or disability caused due an unfortunate accident. The motor insurance policy essentially has a Personal Accident cover for the owner-driver, as per tariff, for which no extra premium is to be paid. For a person other than the owner and driver, the Personal Accident cover has to be purchased separately by paying an additional premium. The amount paid as compensation depends upon the extent of cover opted for.

""",
])

bot1.train([

"""Will I get a Personal Accident cover if the vehicle is registered under someone else's name, but is driven by me and the premium is also paid by me
""",

"""
The policy essentially contains a Personal accident cover for the owner-driver, as per tariff. In case of un-named driver, the personal accident cover has to be purchased separately by paying an additional premium.

""",
])

bot1.train([

"""Will I be eligible for any discounts if I am a member of the Automobile Association of India
""",

"""
Yes, as a member of any of the following recognized Automobile Associations, a discount on Own Damage (OD) premium is given under the policy. The following Associations are recognized:

• The Automobile Association of Eastern India
• The Uttar Pradesh Automobile Association
• The Western India Automobile Association
• The Automobile Association of Southern India
• The Automobile Association of Upper India

""",
])

bot1.train([

"""Is there any discount available if I install an Anti-theft alarm and Locking system
""",

"""
If your vehicle is fitted with anti theft devices, which are approved by the Automobile Research Association of India (ARAI), a discount on Own Damage (OD) premium is allowed.

""",
])
bot1.train([
"""What is Accident Cover for un-named passengers
""",

"""
Passengers other than the insured, including a paid driver and cleaner of the vehicle can be insured under this cover by paying an additional premium. This covers them against death or disability caused due an unfortunate accident.

""",
])
bot1.train([

"""How is the value of the vehicle (IDV - Insured Declare Value) determined
""",

"""
The IDV of the vehicle is to be fixed based on the manufacturer's listed selling price of the brand and model, as the vehicle proposed for insurance at the commencement of insurance /renewal and adjusted for depreciation. 

The IDV of the side car(s) and/ or accessories, if any, fitted to the vehicle, but not included in the manufacturer's listed selling price of the vehicle is also likewise to be fixed. The schedule of depreciation for arriving at IDV is as below:

	Schedule Of Depreciation For Arriving At IDV
---------------------------------------------Age Of The Vehicle    -----	% Of Depreciation Fixing IDV---------------------------------------------------------
## Not exceeding 6 months	--- 5% 																								
## Exceeding 6 months but not exceeding 1 year ---	15%
## Exceeding 1 year but not exceeding 2 years	--- 20%
## Exceeding 2 years but not exceeding 3 years ---	30%
## Exceeding 3 years but not exceeding 4 years	--- 40%
## Exceeding 4 years but not exceeding 5 years	--- 50%



""", ])


bot1.train([
"""What are electrical and non-electrical accessories? How to calculate the value of accessories?""",

"""Electrical accessories: Any electrical and/or electronic equipment that is not factory fitted with the vehicle can be covered under electrical accessories at an additional premium of 4% on the value of such fitting. Value of electrical accessories will be as declared by the insured. For example, a Music System that is installed in the car after purchase of the vehicle can be covered.Non-electrical accessories: Any Non-electrical/ Non-electronic equipment that is not factory fitted with the vehicle can be covered under non-electrical accessories at an additional premium of invoice value*. Value of non-electrical accessories should be the Invoice value of the non-electrical accessories up to the maximum limit of ` 20,000. For example, Mag wheels and/ or leather seats that are installed in the car after purchase of the vehicle can be covered. * Own damage rate""",

])

bot1.train([
""" If I have a LPG/ CNG kit fitted in the car that is not endorsed in the RC, can I take a policy?
""",

"""Policy will only be issued if the LPG/ CNG kit is duly endorsed on the RC (Registration Certificate) by the concerned RTO.
""",


])

bot1.train([
"""What is Voluntary deductible?
""",

"""Voluntary deductible is the amount you opt for higher deductible over and above the compulsive deductible in the event of the claim. (Final Claim amount will be after deduction of depreciation on parts, VD and compulsory deductible as per IMT)
Please find below the voluntary deductible options avialable with car insurance :  
""",


])

bot1.train([
"""What is the process for obtaining Third Party only cover?
""",

"""To issue only Third Party cover, our local underwriter needs to carry out a risk assessment which cannot be done online. Thus, we request the customer to visit us at the nearest branch.
""",


])

bot1.train([
"""What are the events covered in the ICICI Lombard Two Wheeler policy?
""",

"""The ICICI Lombard Two Wheeler policy is a comprehensive vehicle insurance cover, which offers you cover against:
* Any Loss or damage to your vehicle
* Third Party Liability
* Any permanent injury/death to a person caused by your insured vehicle
* Any damage caused to the property other than property belonging to the insured or held in trust or in custody or control of the insured by your vehicle
* A Personal Accident Cover for the owner-driver of the vehicle while s/he is driving

In case of loss or damage to the vehicle or the accessories insured, the Company offers you a cover if the accident occurs due to the following hazards:
* Fire, explosion, self ignition or lightning
* Burglary, housebreaking or theft
* Riot and strike
* Earthquake (fire and shock damage)
* Flood, typhoon, hurricane, storm, tempest, inundation, cyclone, hailstorm, frost
* Accident by external means
* Malicious act
* Terrorist activity
""",
])

bot1.train([
"""Whilst in transit by road, rail, inland-waterway, lift, elevator or air
""",

""" Landslide and rockslide
""",

""" What is the Accident Cover for un-named passengers?
""",

"""Passengers other than the insured, namely, the co-passenger/pillion rider, can be insured under this cover by paying an additional premium. This covers them against death or disability caused due an unfortunate accident.

""",


])

bot1.train([
"""What are the factors affecting the premium amount?
""",

"""The premium payable for your vehicle depends on the below factors:  
* Cubic capacity of the engine 
* Age of vehicle
* Geographical Zone
    $ Type of Model   
    * IDV (Insured declared Value)
"""
])

bot1.train([

"""What is ARAI?
""",

"""ARAI stands for Automotive Research Association of India. If you have installed an ARAI approved anti-theft device in your vehicle, whose installation is dully certified by the agency, you can get a discount of 2.5% on the OD (Own Damage) premium subject to maximum of ₹500.
""",


])

bot1.train([
"""What are the different modes of payment on icicilombard.com?
""",

"""You can choose between 6 payment options to pay your premium online:

*Credit Card – Make secure premium payment with your VISA, Master and AMEX card. 

* Net Banking - Transfer the premium amount online through ICICI Bank and 13 other selected Banks


*Debit Card – Just enter your Citibank, HDFC Bank, ICICI Bank or any of the other 7 approved bank’s Debit Card details to pay your insurance premium directly


*Cash Card - Use your Done or ITZ Card to make the payment online


*Cheque/ Demand Draft: You can send a Cheque/ Demand Draft by courier to our office address
""",


""" How do I register my claim?
""",

"""Contact our Toll Free Helpline 1800 2666 to register your claim and get a claim number/ reference number. You can also directly register your claim online*, with our Lodge A Motor Claim service.

# # Please note that as of now, only accidental damage claims can be processed through the 'Lodge A Motor Claim' interface
""",
])

bot1.train([
"""When should I report to the police?
""",

"""Incidents such as "Third Party Property Damage", "Bodily Injury To Self or Third Party" or "Theft" should be reported to the nearest police station as early as possible, under whose jurisdiction the incident has occurred.
""",


])

bot1.train([
"""What is Cashless Claim and Non-cashless/ Reimbursement claim?
""",

"""Cashless Claim : In cashless claim facility, the repair charges of the vehicle are directly paid to the garage by us, provided the vehicle is repaired in our garage network.

* Non-cashless/ Reimbursement : If the vehicle is repaired in a garage outside the purview of our network, then you will be liable to pay the repair charges of the garage. You can get your claim amount reimbursed by submitting the original bills and payment receipts to our office.
""",

])

bot1.train([
"""What is the claim procedure adopted by the company for settlements?
""",

"""ICICI Lombard adopts the following process for settlement of claim:

## For Cashless claim settlement -

* The Customer Relationship Manager (CRM) / Surveyor attends the claim within 24 hours of registering the claim


* Insured must fill the claim form, (click here to download it or collect it from the CRM/ Surveyor/ Dealer) and submit all the required documents to the CRM/ Surveyor/ Dealer
 

* Our CRM will get the estimate for the repairs of insured vehicle and give spot approval after assessment
 
*  After the completion of repairs at our preferred garage, we will make the payment of our share of the loss directly to the garage. Any amount over and above the admissible amount will have to be directly paid by the Insured
 

* The amount of Depreciation as per the rate prescribed under the Indian Motor Tariff and Compulsory Deductions under the policy need to be borne by the Insured

## For Non-cashless/ Reimbursement claim settlement -
 

* The Customer Relationship Manager (CRM) / Surveyor attends the claim within 24 hours of registering the claim


* Insured must fill the claim form (click here to download it or collect it from CRM/ Surveyor/ Dealer) and submit all the required documents to the CRM/ Surveyor/ Dealer
 
* The CRM/ Surveyor assess the loss, estimates the repair amount and then informs the Insured on the same day of assessment. The CRM/ Surveyor will also take photographs of the damaged vehicle
 

* Insured can then get the vehicle repaired at preferred workshop/ garage. The CRM later carries out a re-inspection of the vehicle. The Insured then pays the workshop/ garage as per the CRM/ Surveyor’s assessed estimation, who thereafter releases a ‘Proof of Release’ document. (The proof of release is an authenticated document signed by the insured to release his vehicle from the garage after it is checked and repaired)
 

* Insured needs to submit the original bill, proof of release and cash receipt (derived from the garage) to the CRM/ Surveyor
 

* The CRM/ Surveyor then submits all required documents to ICICI Lombard for settlement of the claim
 

* Upon acceptance of the claim, the company issues the cheque to the Insured within seven working days from the date of receipt of all documents
 
 ## The amount of Depreciation as per the rate prescribed under the Indian Motor Tariff and Compulsory Deductions under the policy need to be borne by the Insured
""",
])


bot1.train([
"""What documents are required to file a claim?
""",
"""
In case of accidental damages claim, you need to provide the following documents:
 * Claim Form duly signed

*  Valid R.C. copy of the vehicle

*  Valid driving license copy,

 * Policy copy

* FIR, if required (For Theft, Third Party Injury/ Damage; Highway accidents - Major only)


## Original repair bill, proof of release and cash receipt

* Any other document as required to investigate the Claim or Company's obligation to make payment for it

""",

"""
Please provide me with the list of garages in my city where I can avail Cashless service?
""",

"""
Click here to search and view the list of garages in your city where you can avail Cashless service
""",


])

bot1.train([
"""What is the meaning of deductibles? What is the deductible applicable to Private Car and Two-wheeler?
""",

"""Deductible means the amount that you will bear in case of a claim. This amount is deducted from the claim amount. Car Insurance Policy carries a Compulsory Deductible of ` 1,000 (for vehicles not exceeding 1500 cc) or ` 2,000/- (for vehicles exceeding 1500 cc). Two-wheeler Insurance policies carry a Compulsory Deductible of ` 100.
""",


])

bot1.train([
"""What is meant by Constructive Total Loss?
""",

"""Constructive Total Loss refers to accidental loss/ damage to your vehicle where the aggregate cost of retrieval and/ or repairs amounts to be more than 75% of the Insured's Declared Value (IDV) on your policy.
""",

""" If I lodge a claim after the expiry of my policy date for an event that occurred during the policy period, will it still be valid?
""",

"""Yes, you will be eligible for the claim even after the expiry of the policy date. This is because the event took place during the policy period.
""",

])

bot1.train([
"""What if I fail to produce the required documents?
""",

"""There are some documents that are definitely needed, without which a claim will not be paid. We will try and assist you to find surrogate means to get the required proof.
""",
])

bot1.train([

"""Which are the cashless garages available in my city?
""",

"""In case of an accident, when should I report to the police?
""",

"""Incidents such as "Third Party Property Damage", "Bodily Injury to Self or Third Party" or "Theft" should be reported to the nearest police station as early as possible, under whose jurisdiction the incident has occurred.
""",


])

bot1.train([
"""What is an endorsement?
""",

"""An endorsement is a written evidence of an agreed change in the policy. It is a document that incorporates changes in the terms of the policy. Additional premium will charged as applicable.
""",


])

bot1.train([
"""What is a non-premium bearing endorsement?
""",

"""A non-premium bearing endorsement is the endorsement for which no additional premium is charged. For example, Rectification in contact details, Rectification in engine/ chassis number, Addition of hypothecation, etc.
""",


])

bot1.train([
"""What is a premium bearing endorsement?
""",

"""A premium bearing endorsement is the endorsement for which additional premium is charged. For example, Transfer of ownership, Addition of LPG/ CNG kit, Change of RTO location, etc.
""",


""" I want to make changes in my policy
""",

"""
Following changes are allowed in the policy

## Name rectification :

* Please send a mail with the policy details on customersupport@icicilombard.com. You would be provided with a request number and the changes would be done

* You can click here to put in a request
 
* You can also visit our nearest branch with these documents for the same

  "Registration number/ Engine/ Chassis number rectification"

$$  Please send a mail with the policy details and a scanned copy of your RC book on customersupport@icicilombard.com. You would be provided with a request number and the changes would be done

* You can click here to put in a request and upload a scanned copy of your RC book
 
* You can also visit our nearest branch with these documents for the same.

## Address Rectification :

* Please send a mail with the policy details and the correct address details on customersupport@icicilombard.com. You would be provided with a request number and the changes would be done

* You can click here to put in a request and upload a scanned copy of your address proo

* You can also visit our nearest branch with a request letter for the same

## Address change : 
* Please send a mail with the policy details and the correct address details on customersupport@icicilombard.com. You would be provided with a request number and the changes would be done
 
* You can click here to put in a request and upload a scanned copy of your address proof

$$ You can also visit our nearest branch with a request letter for the same

Change in model/Vehicle

$$ Please visit our nearest branch with a copy of your RC book, request letter and policy documents. These changes might affect the premium charged, so please carry a cheque along.

Name transfer (Transfer of ownership)

* If you transfer your vehicle on some other person’s name, the insurance also needs to be transferred on the new owner’s name.
 

##  To get the insurance transferred in the new owner’s name, please visit our nearest branch with:
1. Endorsed copy of Registration Certificate/ Form 29 and Form 30 along with seller request letter for transfer of ownership
2. Proposal form filled and signed by the new owner of the vehicle
3. Vehicle inspection report if the difference between the date of transfer and request for endorsement is greater than 14 days
4. These changes might affect the premium charged, so please carry a cheque along

## Addition of LPG/ CNG kit/ Electrical/ Non-electrical accessories: 

Please visit our nearest branch with the following documents:

* Invoice copy of the CNG kit/ Electrical/ Non-electrical accessories and endorsed RC (with LPG/ CNG) or letter with the declaration value

* Request letter

* Cheque for paying the required premium

## Addition of Anti-theft device: 

$$ Please visit our nearest branch with the following documents:


* Invoice copy of fitted device (ARAI approved) or letter with the declaration value

* Request letter

## Change in RTO/ Registration :

* Please visit our nearest branch with the following documents:

* Copy of your updated endorsed Registration Certificate (RC)
 

* These changes might affect the premium charged, so please carry a cheque along.

## NCB Recovery/ Change :
 
$$ Please visit our nearest branch with the following documents:
 

* Request letter from Insured
 

* Original NCB reserving letter from Previous Insurer
 
*  Proof of sale of old vehicle

## Addition of Hypothecation :
 

* Please send a mail with the policy details, a scanned copy of your request letter, your sanction letter from the financial institution and the endorsed copy of your Registration Certificate (RC) on customersupport@icicilombard.com. You would be provided with a request number and the changes would be done
 

* You can click here to put in a request and upload the scanned copy of request letter, your sanction letter from the financial institution and the endorsed copy of Registration Certificate
 

 $$ You can also visit our nearest branch with these documents for the same

## Change of Hypothecation

 $$ Please send a mail with the policy details, a scanned copy of Request letter, your sanction letter from the new financial institution, NOC from the previous financial institution and the endorsed copy of Registration Certificate on customersupport@icicilombard.com. You would be provided with a request number and the changes would be done

 $$ You can click here to put in a request and upload the scanned copy of Request letter, your sanction letter from the new financial institution, NOC from the previous financial institution and the endorsed copy of Registration Certificate

 $$ You can also visit our nearest branch with these documents for the same

## Cancellation of hypothecation: 

*  Please send a mail with the policy details and a scanned copy of Request letter, your NOC letter from the financial institution documents and the endorsed copy of Registration Certificate on customersupport@icicilombard.com. You would be provided with a request number and the changes would be done

* You can click here to put in a request and upload the scanned copy of Request letter, your NOC letter from the financial institution documents and the endorsed copy of Registration Certificate
*  You can also visit our nearest branch with these documents for the same
""",

""" Website
""",
"""
icicibank.com
""",
])