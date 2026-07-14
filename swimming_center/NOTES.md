# Project Hallenbad

this file is only for intern use.  
the file README should be created by AI-Assistant from VSCode.  

## Intro / Requirements / References

Coding language is english  
Programmign language is python3  

https://www.mockaroo.com/  

## logical professional optimal sequence

0. get to know the client and let him tell you an history
1. meeting for user stories and to collect requirements
2. create use cases
3. from use cases, create your diagramms
4. then code it
5. then test it
6. then loop it proactively

## Our Mission

* code a project
* write class diagramm
* write sequance diagramm
* write activity diagramm
* the code must run
* present the runnable code to the others

[ ] TODO : bring it to git / software ideas, when done!

## how to presentate it to our loved colleagues ?!?!?

1. a flow chart with the idea
2. an image of swimming center and what interest, what doesn't
3. class and activity
4. code
5. sequence
6. code

## Organisation

### Client data from mockarro

age:  
n = random(1,100)  
if n < 25 then random(1,10)  
elsif n < 35 then random(10,18)  
elsif n < 75 then random(18,45)  
elsif n < 90 then random(45,65)  
elsif n < 98 then random(65,85)  
else random(85,100) end  

subscription:  
if random(1,100) < 20 then 1 else 0 end  

### Employees data from Mockarro

gender:  
if random(1,10) < 7 then "Male" else "Female" end  

age:  
n = random(1,100)  
if n < 15 then random(15,21)  
elsif n < 85 then random(21,55)  
else random(55,65) end  

position:  
if field('age') <= 21 and random(1,10) < 8 then "Azubi"  
elsif random(1,10) < 2 then "Pool Master"  
else "Employee" end  




### Classes

Enum Areas [Entrance, Child, Swimming, Sauna]

Class Area
    
    name: ENUM[Areas]

Class TicketSystem:

    number: integer, 
    client_number: Integer,
    created_at: integer (unix timestamp), 
    checkin_at: integer (unix timestamp), 
    checkout_at: integer (unix timestamp), 
    permitted_areas: List[String]

Class SwimmingCenter

    name: String
    description: String
    address: String
    opening_time: String

    Komposition by areas (Class Area) -> must have:  
        * entrance area
        * child pool
        * swimming pool
        * sauna
        * organisational class - Class TicketSystem

        HINTS:
            all Tickets are day cards
            the swimming center is opened from 06:00 to 22:00 (extended working hours)
            we need a DB (as an imported dictionary by ticket number) to register the tickets


Class Client

    number: Integer
    ticket_number: Integer (Association by Ticket - from class Ticket)

    HINTS:
        get ticket description from ticket database by number
        Subclass: Subscription Client, Casual Client

Class Subscription(Client):
    begin_subscriptio: Integer (unix timestamp)
    end_subscriptio: Integer (unix timestamp)

Class Casual(Client):
    pass



Class Automatic (this is the sell maschine for the tickets)

    number: Integer
    buy_options: ENUM[Areas]

    create_ticket() -> Ticket()
        create Ticket() at database
        write ticket number at Client.ticket_number

    sell(option, money) -> None:
        if money >= price:
            create_ticket()
        else:
            Message: "please insert more money"
            Option: "Cancel"


Class Employee (they are the life guards)
    name: String
    number: Integer
    working_turn: String [morning, afternoon, evening]

    lifeguard_blew_the_whistle() -> String:
        return "Tweet, tweet, tweet! Don't do it."

    lifeguard_invites_you_to_go_out() -> String:
        return "Please leave the Swimming Center now!"