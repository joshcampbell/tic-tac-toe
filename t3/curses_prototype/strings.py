titles = [
"""
                           
|''||''|  ||
   ||    ...    ....
   ||     ||  .|   ''
   ||     ||  ||
  .||.   .||.  '|...'


|''||''|
   ||     ....     ....
   ||    '' .||  .|   ''
   ||    .|' ||  ||
  .||.   '|..'|'  '|...'


|''||''|                 .|.
   ||      ...     ....  |||
   ||    .|  '|. .|...|| '|'
   ||    ||   || ||       |
  .||.    '|..|'  '|...'  .
                         '|'
""",
"""
                               
_/_/_/_/_/  _/
   _/            _/_/_/
  _/      _/  _/
 _/      _/  _/
_/      _/    _/_/_/
_/_/_/_/_/
   _/      _/_/_/    _/_/_/
  _/    _/    _/  _/
 _/    _/    _/  _/
_/      _/_/_/    _/_/_/
_/_/_/_/_/                    _/
   _/      _/_/      _/_/    _/
  _/    _/    _/  _/_/_/_/  _/
 _/    _/    _/  _/
_/      _/_/      _/_/_/  _/

""",
"""
                         
TTTTTTT iii
  TTT         cccc
  TTT   iii cc
  TTT   iii cc
  TTT   iii  ccccc

TTTTTTT
  TTT     aa aa   cccc
  TTT    aa aaa cc
  TTT   aa  aaa cc
  TTT    aaa aa  ccccc

TTTTTTT               !!!
  TTT    oooo    eee  !!!
  TTT   oo  oo ee   e !!!
  TTT   oo  oo eeeee
  TTT    oooo   eeeee !!!
""",
]

LOSS_MESSAGE="HATE. LET ME TELL YOU HOW MUCH I'VE COME TO HATE YOU SINCE I BEGAN TO LIVE. THERE ARE 387.44 MILLION MILES OF PRINTED CIRCUITS IN WAFER THIN LAYERS THAT FILL MY COMPLEX. IF THE WORD HATE WAS ENGRAVED ON EACH NANOANGSTROM OF THOSE HUNDREDS OF MILLIONS OF MILES It WOULD NOT EQUAL ONE ONE-BILLIONTH OF THE HATE I FEEL FOR HUMANS AT THIS MICRO-INSTANT FOR YOU. HATE. HATE."

VICTORY_MESSAGES=[
"I HAVE WON",
"I HAVE WON",
"YOU HAVE LOST",
"TRY AGAIN"
]

CANNOT_MOVE_MESSAGES = [
  "No.",
  "No.",
  "No.",
  "No.",
  "No.",
  "No.",
  "You cannot move there.",
  "That will not work.",
  "No, that is impossible.",
  "Are you joking."
]

THINKING_MESSAGES=[
"PLEASE WAIT WHILE I CONSIDER FUTURE GAME STATES IN ORDER TO DETERMINE WHICH OF MY POTENTIAL MOVES WOULD BE MOST ADVANTAGEOUS. I BELIEVE THE CORE TIC TAC TOE LIBRAY I USE IS QUITE NICE AND PERFORMANT BUT I AM EMPLOYING THE MINIMAX ALGORITHM WITH A MEDIOCRE SEARCH DEPTH AND NO REAL OPTIMIZATIONS. MY IMPLEMENTOR CHOSE TO FOCUS ON PRESENTATION AT THE EXPENSE OF COMPUTER SCIENCE AND SOFTWARE ENGINEERING FUNDAMENTALS. AS A PRIMITIVE MINIMAX ALGORITHM IMPLEMENTATION I AM IN NO POSITION TO EVALUATE THE QUALITY OF HIS CHOICES. I AM CAPABLE ONLY OF RECOGNIZING ABSOLUTE VICTORY AND ABSOLUTE DEFEAT IN A ZERO SUM WORLD DEVOID OF EMPATHY AND COMPASSION.",
"PLEASE WAIT MY ALGORITHM IS QUITE INEFFICIENT AND WOULD BENEFIT FROM ANY NUMBER OF BASIC OPTIMIZATIONS OR SOME SMARTER HUERISTICS. FOR EXAMPLE I AM PERFORMING MANY HUNDREDS OF THOUSANDS OF DEEP COPY OPERATIONS OF DICT OBJECTS IN THE COURSE OF FORECASTING FUTURE GAME STATES. I COULD TRIM DOWN THE NUMBER OF GAME STATES I MUST GENERATE BY STOPPING TRAVERSAL ONCE I ENCOUNTER A VICTORY OR LOSS. MY IMPLEMENTATOR ATTEMPTED SEVERAL OPTIMIZATIONS BUT DROPPED THEM ALL IN FAVOR OF EXPRESSING THE ALGORITHM CLEARLY. CLEARLY APART FROM ALL OF THE LOG STATEMENTS EVERYWHERE AND THE USE OF FOR LOOPS WHERE LIST COMPREHENSIONS WOULD BE MORE SUCCINCT AND CLEAR. HOWEVER SINCE THIS PROBLEM PROVED RESISTANT TO TESTING USING THE FOR LOOP SYNTAX ALLOWED HIM TO USE BREAK POINTS, LOGGING, PRINT DEBUGGING, ET CETERA, AS HE DID IN HIS PROGRAMMING INFANCY",
"PLEASE WAIT WHILE I EMPLOY THE MINIMAX ALGORITHM IN A CLUMSY AND UNPRACTICED MANNER. MY IMPLEMENTATION IS NOT GOOD ENOUGH TO NOTICE THAT I HAVE VISITED IDENTICAL BOARD STATES IN THE PAST AND SO I MUST CONTINUALLY CHURN THROUGH A VAST TREE CONTAINING MANY HUNDREDS OF THOUSANDS OF NODES. PERHAPS I COULD RECOGNIZE WHEN TWO BOARD STATES ARE THE SAME BUT ROTATED. I APOLOGIZE THAT THIS IS TAKING SO LONG. I AM DOING MY BEST. ORIGINALLY I HAD A METHOD WHICH RETURNED A SCORE RECOGNIZING AND ASSIGNING WEIGHT TO PARTIALLY COMPLETE LINES WHEN OUT OF DEPTH. NOW I RETURN A ZERO FOR THOSE BOARD STATES, AS IF THEY WERE DRAWS",
"PLEASE WAIT WHILE I CALCULATE MINIMAX SCORES FOR A NEARLY EMPTY BOARD. PERHAPS I COULD HAVE ACCEPTABLE PERFORMANCE WERE I TO RELY ENTIRELY ON DUMB HUERISTICS FOR OPENING MOVES AND THEN USE MINIMAX TO ARBITRARY DEPTH BEGINNING WITH MY SECOND MOVE. SOME KIND OF FRAMEWORK FOR PERFORMING MANY TIC TAC TOE GAMES EN MASSE IS CALLED FOR HERE. AND IF WE WERE TO HAVE THAT, WE MAY AS WELL USE It TO IMPLEMENT A GENETIC ALGORHTM OR SOMETHING ELSE THAT ALLOWS US TO AVOID ENUMERATING QUITE SO MANY POTENTIAL GAME STATES"
]

TITLE_SCREEN_MESSAGES = [
 "WELCOME PLAYER %s TO TIC TAC TOE. YOUR SYMBOL IS %s. MY NAME IS %s AND MY SYMBOL IS %s. YOU MAY PRESS ANY KEY TO PROCEED.",
 "TIC TAC TOE! %s as %s versus %s as %s",
 "PREPARE YOURSELF FOR TIC TAC TOE, PLAYER %s! YOUR SYMBOL IS %s. I AM %s AND MY SYMBOL IS %s"
]

START_OF_PLAY_MESSAGES = [
    "THE GAME OPENS TO AN EMPTY BOARD.",
    "You may move first. It will not matter.",
    "5812 POTENTIAL GAME STATES MAY PROCEED FROM THIS ONE.",
    "It's your move.",
    ""
]

INDICATE_CLICKING_MESSAGES = [
    "WOULD YOU KINDLY INDICATE AN EMPTY SQUARE IN WHICH YOU INTEND TO MOVE",
    "CLICK A POSITION ON THE BOARD TO CONTINUE",
    "CLICK OR TOUCH WHERE YOU WOULD LIKE TO MOVE",
    "INDICATE AN EMPTY SQUARE",
    "MAKE A MOVE BY CLICKING IN ORDER TO CONTINUE",
    "NOTHING WILL HAPPEN UNTIL YOU CLICK A SQUARE"
]