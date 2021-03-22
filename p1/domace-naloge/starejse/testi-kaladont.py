# Tu napiši svoje funkcije

...



import unittest


class Obvezna(unittest.TestCase):
    def test_lahko_sledi(self):
        self.assertTrue(lahko_sledi("OMARA", "ASPARAGUS"))
        self.assertTrue(lahko_sledi("PETER", "REBEKA"))
        self.assertFalse(lahko_sledi("PETER", "ASPARAGUS"))
        self.assertFalse(lahko_sledi("PRETEP", "PRETEP"))

    def test_izberi_besedo(self):
        self.assertEqual(
            "RAZBOJNIK", izberi_besedo("PETER",
                                       ["RAZBOJNIK", "ROPAR", "RAVBAR", "TAT",
                                        "ŽEPAR", "OTORINOLARINGOLOGIJA"]))
        self.assertEqual(
            "RAZBOJNIK", izberi_besedo("PETER",
                                       ["ROPAR", "RAVBAR", "RAZBOJNIK", "TAT",
                                        "ŽEPAR", "OTORINOLARINGOLOGIJA"]))
        self.assertEqual(
            "RAVBAR", izberi_besedo("PETER",
                                    ["ROPAR", "RAVBAR", "TAT", "ROLAND",
                                     "ŽEPAR", "OTORINOLARINGOLOGIJA"]))
        self.assertEqual(
            "RAVBAR", izberi_besedo("PETER", ["ROPAR", "ROLAND", "TAT",
                                              "OTORINOLARINGOLOGIJA", "RAVBAR",
                                              "ŽEPAR"]))
        self.assertEqual(
            "PETER", izberi_besedo("PRETEP",
                                   ["PETER", "OTORINOLARINGOLOGIJA", "PRETEP",
                                    "PERO", "MAFIJA"]))

    def test_ni_ponavljanj(self):
        self.assertTrue(ni_ponavljanj(["PETER", "ŽOGA", "METLA", "JOŽE"]))
        self.assertTrue(ni_ponavljanj(["PETER"]))
        self.assertTrue(ni_ponavljanj([]))

        self.assertFalse(ni_ponavljanj(["PETER", "PETER"]))
        self.assertFalse(ni_ponavljanj(["PETER", "ŽOGA", "JOŽE", "JOŽE"]))
        self.assertFalse(ni_ponavljanj(["PETER", "ŽOGA", "JOŽE", "ŽOGA"]))
        self.assertFalse(ni_ponavljanj(["PETER", "ŽOGA", "JOŽE", "PETER"]))
        self.assertFalse(ni_ponavljanj(["PETER", "ŽOGA", "PETER", "JOŽE"]))

    def test_preveri_zaporedje(self):
        self.assertTrue(preveri_zaporedje(
            ["PETER", "RAZBOJNIK", "KLEMEN", "NEPRIDIPRAV", "VINKO",
             "OROŽNIK"]))
        self.assertTrue(preveri_zaporedje(["PETER", "RAZBOJNIK"]))
        self.assertTrue(preveri_zaporedje(["VINKO"]))

        self.assertFalse(
            preveri_zaporedje(["PETER", "ZABOJNIK", "KLEMEN", "NEPRIDIPRAV"]))
        self.assertFalse(
            preveri_zaporedje(["PETER", "RAZBOJNIK", "ALEŠ", "NEPRIDIPRAV"]))
        self.assertFalse(
            preveri_zaporedje(["PETER", "RAZBOJNIK", "KLEMEN", "TAT"]))
        self.assertFalse(
            preveri_zaporedje(["PETER", "RAZBOJNIK", "KLEP", "PETER", "RIBA"]))


class TestDodatna(unittest.TestCase):
    slovar = ["ABRAHAM", "MELODIJA", "ASTEROID", "DREVO", "MEČ", "OBLAK",
              "KLEPTOMAN", "KAČA", ]

    nouns = ['PEOPLE', 'HISTORY', 'WAY', 'ART', 'WORLD', 'INFORMATION', 'MAP',
             'TWO', 'FAMILY', 'GOVERNMENT', 'HEALTH', 'SYSTEM', 'COMPUTER',
             'MEAT', 'YEAR', 'THANKS', 'MUSIC', 'PERSON', 'READING', 'METHOD',
             'DATA', 'FOOD', 'UNDERSTANDING', 'THEORY', 'LAW', 'BIRD',
             'LITERATURE', 'PROBLEM', 'SOFTWARE', 'CONTROL', 'KNOWLEDGE',
             'POWER', 'ABILITY', 'ECONOMICS', 'LOVE', 'INTERNET', 'TELEVISION',
             'SCIENCE', 'LIBRARY', 'NATURE', 'FACT', 'PRODUCT', 'IDEA',
             'TEMPERATURE', 'INVESTMENT', 'AREA', 'SOCIETY', 'ACTIVITY',
             'STORY', 'INDUSTRY', 'MEDIA', 'THING', 'OVEN', 'COMMUNITY',
             'DEFINITION', 'SAFETY', 'QUALITY', 'DEVELOPMENT', 'LANGUAGE',
             'MANAGEMENT', 'PLAYER', 'VARIETY', 'VIDEO', 'WEEK', 'SECURITY',
             'COUNTRY', 'EXAM', 'MOVIE', 'ORGANIZATION', 'EQUIPMENT', 'PHYSICS',
             'ANALYSIS', 'POLICY', 'SERIES', 'THOUGHT', 'BASIS', 'BOYFRIEND',
             'DIRECTION', 'STRATEGY', 'TECHNOLOGY', 'ARMY', 'CAMERA', 'FREEDOM',
             'PAPER', 'ENVIRONMENT', 'CHILD', 'INSTANCE', 'MONTH', 'TRUTH',
             'MARKETING', 'UNIVERSITY', 'WRITING', 'ARTICLE', 'DEPARTMENT',
             'DIFFERENCE', 'GOAL', 'NEWS', 'AUDIENCE', 'FISHING', 'GROWTH',
             'INCOME', 'MARRIAGE', 'USER', 'COMBINATION', 'FAILURE', 'MEANING',
             'MEDICINE', 'PHILOSOPHY', 'TEACHER', 'COMMUNICATION', 'NIGHT',
             'CHEMISTRY', 'DISEASE', 'DISK', 'ENERGY', 'NATION', 'ROAD', 'ROLE',
             'SOUP', 'ADVERTISING', 'LOCATION', 'SUCCESS', 'ADDITION',
             'APARTMENT', 'EDUCATION', 'MATH', 'MOMENT', 'PAINTING', 'POLITICS',
             'ATTENTION', 'DECISION', 'EVENT', 'PROPERTY', 'SHOPPING',
             'STUDENT', 'WOOD', 'COMPETITION', 'DISTRIBUTION', 'ENTERTAINMENT',
             'OFFICE', 'POPULATION', 'PRESIDENT', 'UNIT', 'CATEGORY',
             'CIGARETTE', 'CONTEXT', 'INTRODUCTION', 'OPPORTUNITY',
             'PERFORMANCE', 'DRIVER', 'FLIGHT', 'LENGTH', 'MAGAZINE',
             'NEWSPAPER', 'RELATIONSHIP', 'TEACHING', 'CELL', 'DEALER',
             'FINDING', 'LAKE', 'MEMBER', 'MESSAGE', 'PHONE', 'SCENE',
             'APPEARANCE', 'ASSOCIATION', 'CONCEPT', 'CUSTOMER', 'DEATH',
             'DISCUSSION', 'HOUSING', 'INFLATION', 'INSURANCE', 'MOOD', 'WOMAN',
             'ADVICE', 'BLOOD', 'EFFORT', 'EXPRESSION', 'IMPORTANCE', 'OPINION',
             'PAYMENT', 'REALITY', 'RESPONSIBILITY', 'SITUATION', 'SKILL',
             'STATEMENT', 'WEALTH', 'APPLICATION', 'CITY', 'COUNTY', 'DEPTH',
             'ESTATE', 'FOUNDATION', 'GRANDMOTHER', 'HEART', 'PERSPECTIVE',
             'PHOTO', 'RECIPE', 'STUDIO', 'TOPIC', 'COLLECTION', 'DEPRESSION',
             'IMAGINATION', 'PASSION', 'PERCENTAGE', 'RESOURCE', 'SETTING',
             'AD', 'AGENCY', 'COLLEGE', 'CONNECTION', 'CRITICISM', 'DEBT',
             'DESCRIPTION', 'MEMORY', 'PATIENCE', 'SECRETARY', 'SOLUTION',
             'ADMINISTRATION', 'ASPECT', 'ATTITUDE', 'DIRECTOR', 'PERSONALITY',
             'PSYCHOLOGY', 'RECOMMENDATION', 'RESPONSE', 'SELECTION', 'STORAGE',
             'VERSION', 'ALCOHOL', 'ARGUMENT', 'COMPLAINT', 'CONTRACT',
             'EMPHASIS', 'HIGHWAY', 'LOSS', 'MEMBERSHIP', 'POSSESSION',
             'PREPARATION', 'STEAK', 'UNION', 'AGREEMENT', 'CANCER', 'CURRENCY',
             'EMPLOYMENT', 'ENGINEERING', 'ENTRY', 'INTERACTION', 'MIXTURE',
             'PREFERENCE', 'REGION', 'REPUBLIC', 'TRADITION', 'VIRUS', 'ACTOR',
             'CLASSROOM', 'DELIVERY', 'DEVICE', 'DIFFICULTY', 'DRAMA',
             'ELECTION', 'ENGINE', 'FOOTBALL', 'GUIDANCE', 'HOTEL', 'OWNER',
             'PRIORITY', 'PROTECTION', 'SUGGESTION', 'TENSION', 'VARIATION',
             'ANXIETY', 'ATMOSPHERE', 'AWARENESS', 'BATH', 'BREAD', 'CANDIDATE',
             'CLIMATE', 'COMPARISON', 'CONFUSION', 'CONSTRUCTION', 'ELEVATOR',
             'EMOTION', 'EMPLOYEE', 'EMPLOYER', 'GUEST', 'HEIGHT', 'LEADERSHIP',
             'MALL', 'MANAGER', 'OPERATION', 'RECORDING', 'SAMPLE',
             'TRANSPORTATION', 'CHARITY', 'COUSIN', 'DISASTER', 'EDITOR',
             'EFFICIENCY', 'EXCITEMENT', 'EXTENT', 'FEEDBACK', 'GUITAR',
             'HOMEWORK', 'LEADER', 'MOM', 'OUTCOME', 'PERMISSION',
             'PRESENTATION', 'PROMOTION', 'REFLECTION', 'REFRIGERATOR',
             'RESOLUTION', 'REVENUE', 'SESSION', 'SINGER', 'TENNIS', 'BASKET',
             'BONUS', 'CABINET', 'CHILDHOOD', 'CHURCH', 'CLOTHES', 'COFFEE',
             'DINNER', 'DRAWING', 'HAIR', 'HEARING', 'INITIATIVE', 'JUDGMENT',
             'LAB', 'MEASUREMENT', 'MODE', 'MUD', 'ORANGE', 'POETRY', 'POLICE',
             'POSSIBILITY', 'PROCEDURE', 'QUEEN', 'RATIO', 'RELATION',
             'RESTAURANT', 'SATISFACTION', 'SECTOR', 'SIGNATURE',
             'SIGNIFICANCE', 'SONG', 'TOOTH', 'TOWN', 'VEHICLE', 'VOLUME',
             'WIFE', 'ACCIDENT', 'AIRPORT', 'APPOINTMENT', 'ARRIVAL',
             'ASSUMPTION', 'BASEBALL', 'CHAPTER', 'COMMITTEE', 'CONVERSATION',
             'DATABASE', 'ENTHUSIASM', 'ERROR', 'EXPLANATION', 'FARMER', 'GATE',
             'GIRL', 'HALL', 'HISTORIAN', 'HOSPITAL', 'INJURY', 'INSTRUCTION',
             'MAINTENANCE', 'MANUFACTURER', 'MEAL', 'PERCEPTION', 'PIE', 'POEM',
             'PRESENCE', 'PROPOSAL', 'RECEPTION', 'REPLACEMENT', 'REVOLUTION',
             'RIVER', 'SON', 'SPEECH', 'TEA', 'VILLAGE', 'WARNING', 'WINNER',
             'WORKER', 'WRITER', 'ASSISTANCE', 'BREATH', 'BUYER', 'CHEST',
             'CHOCOLATE', 'CONCLUSION', 'CONTRIBUTION', 'COOKIE', 'COURAGE',
             'DAD', 'DESK', 'DRAWER', 'ESTABLISHMENT', 'EXAMINATION', 'GARBAGE',
             'GROCERY', 'HONEY', 'IMPRESSION', 'IMPROVEMENT', 'INDEPENDENCE',
             'INSECT', 'INSPECTION', 'INSPECTOR', 'KING', 'LADDER', 'MENU',
             'PENALTY', 'PIANO', 'POTATO', 'PROFESSION', 'PROFESSOR',
             'QUANTITY', 'REACTION', 'REQUIREMENT', 'SALAD', 'SISTER',
             'SUPERMARKET', 'TONGUE', 'WEAKNESS', 'WEDDING', 'AFFAIR',
             'AMBITION', 'ANALYST', 'APPLE', 'ASSIGNMENT', 'ASSISTANT',
             'BATHROOM', 'BEDROOM', 'BEER', 'BIRTHDAY', 'CELEBRATION',
             'CHAMPIONSHIP', 'CHEEK', 'CLIENT', 'CONSEQUENCE', 'DEPARTURE',
             'DIAMOND', 'DIRT', 'EAR', 'FORTUNE', 'FRIENDSHIP', 'FUNERAL',
             'GENE', 'GIRLFRIEND', 'HAT', 'INDICATION', 'INTENTION', 'LADY',
             'MIDNIGHT', 'NEGOTIATION', 'OBLIGATION', 'PASSENGER', 'PIZZA',
             'PLATFORM', 'POET', 'POLLUTION', 'RECOGNITION', 'REPUTATION',
             'SHIRT', 'SIR', 'SPEAKER', 'STRANGER', 'SURGERY', 'SYMPATHY',
             'TALE', 'THROAT', 'TRAINER', 'UNCLE', 'YOUTH', 'TIME', 'WORK',
             'FILM', 'WATER', 'MONEY', 'EXAMPLE', 'WHILE', 'BUSINESS', 'STUDY',
             'GAME', 'LIFE', 'FORM', 'AIR', 'DAY', 'PLACE', 'NUMBER', 'PART',
             'FIELD', 'FISH', 'BACK', 'PROCESS', 'HEAT', 'HAND', 'EXPERIENCE',
             'JOB', 'BOOK', 'END', 'POINT', 'TYPE', 'HOME', 'ECONOMY', 'VALUE',
             'BODY', 'MARKET', 'GUIDE', 'INTEREST', 'STATE', 'RADIO', 'COURSE',
             'COMPANY', 'PRICE', 'SIZE', 'CARD', 'LIST', 'MIND', 'TRADE',
             'LINE', 'CARE', 'GROUP', 'RISK', 'WORD', 'FAT', 'FORCE', 'KEY',
             'LIGHT', 'TRAINING', 'NAME', 'SCHOOL', 'TOP', 'AMOUNT', 'LEVEL',
             'ORDER', 'PRACTICE', 'RESEARCH', 'SENSE', 'SERVICE', 'PIECE',
             'WEB', 'BOSS', 'SPORT', 'FUN', 'HOUSE', 'PAGE', 'TERM', 'TEST',
             'ANSWER', 'SOUND', 'FOCUS', 'MATTER', 'KIND', 'SOIL', 'BOARD',
             'OIL', 'PICTURE', 'ACCESS', 'GARDEN', 'RANGE', 'RATE', 'REASON',
             'FUTURE', 'SITE', 'DEMAND', 'EXERCISE', 'IMAGE', 'CASE', 'CAUSE',
             'COAST', 'ACTION', 'AGE', 'BAD', 'BOAT', 'RECORD', 'RESULT',
             'SECTION', 'BUILDING', 'MOUSE', 'CASH', 'CLASS', 'NOTHING',
             'PERIOD', 'PLAN', 'STORE', 'SIDE', 'SUBJECT', 'SPACE',
             'RULE', 'STOCK', 'WEATHER', 'CHANCE', 'FIGURE', 'MAN', 'MODEL',
             'SOURCE', 'BEGINNING', 'EARTH', 'PROGRAM', 'CHICKEN', 'DESIGN',
             'FEATURE', 'HEAD', 'MATERIAL', 'PURPOSE', 'QUESTION', 'ROCK',
             'SALT', 'ACT', 'BIRTH', 'CAR', 'DOG', 'OBJECT', 'SCALE', 'SUN',
             'NOTE', 'PROFIT', 'RENT', 'SPEED', 'STYLE', 'WAR', 'BANK', 'CRAFT',
             'HALF', 'INSIDE', 'OUTSIDE', 'STANDARD', 'BUS', 'EXCHANGE', 'EYE',
             'FIRE', 'POSITION', 'PRESSURE', 'STRESS', 'ADVANTAGE', 'BENEFIT',
             'FRAME', 'ISSUE', 'STEP', 'CYCLE', 'FACE', 'ITEM', 'METAL',
             'PAINT', 'REVIEW', 'ROOM', 'SCREEN', 'STRUCTURE', 'VIEW',
             'ACCOUNT', 'BALL', 'DISCIPLINE', 'MEDIUM', 'SHARE', 'BALANCE',
             'BIT', 'BLACK', 'BOTTOM', 'CHOICE', 'GIFT', 'IMPACT', 'MACHINE',
             'SHAPE', 'TOOL', 'WIND', 'ADDRESS', 'AVERAGE', 'CAREER', 'CULTURE',
             'MORNING', 'POT', 'SIGN', 'TABLE', 'TASK', 'CONDITION', 'CONTACT',
             'CREDIT', 'EGG', 'HOPE', 'ICE', 'NETWORK', 'NORTH', 'SQUARE',
             'ATTEMPT', 'DATE', 'EFFECT', 'LINK', 'POST', 'STAR', 'VOICE',
             'CAPITAL', 'CHALLENGE', 'FRIEND', 'SELF', 'SHOT', 'BRUSH',
             'COUPLE', 'DEBATE', 'EXIT', 'FRONT', 'FUNCTION', 'LACK', 'LIVING',
             'PLANT', 'PLASTIC', 'SPOT', 'SUMMER', 'TASTE', 'THEME', 'TRACK',
             'WING', 'BRAIN', 'BUTTON', 'CLICK', 'DESIRE', 'FOOT', 'GAS',
             'INFLUENCE', 'NOTICE', 'RAIN', 'WALL', 'BASE', 'DAMAGE',
             'DISTANCE', 'FEELING', 'PAIR', 'SAVINGS', 'STAFF', 'SUGAR',
             'TARGET', 'TEXT', 'ANIMAL', 'AUTHOR', 'BUDGET', 'DISCOUNT', 'FILE',
             'GROUND', 'LESSON', 'MINUTE', 'OFFICER', 'PHASE', 'REFERENCE',
             'REGISTER', 'SKY', 'STAGE', 'STICK', 'TITLE', 'TROUBLE', 'BOWL',
             'BRIDGE', 'CAMPAIGN', 'CHARACTER', 'CLUB', 'EDGE', 'EVIDENCE',
             'FAN', 'LETTER', 'LOCK', 'MAXIMUM', 'NOVEL', 'OPTION', 'PACK',
             'PARK', 'PLENTY', 'QUARTER', 'SKIN', 'SORT', 'WEIGHT', 'BABY',
             'BACKGROUND', 'CARRY', 'DISH', 'FACTOR', 'FRUIT', 'GLASS', 'JOINT',
             'MASTER', 'MUSCLE', 'RED', 'STRENGTH', 'TRAFFIC', 'TRIP',
             'VEGETABLE', 'APPEAL', 'CHART', 'GEAR', 'IDEAL', 'KITCHEN', 'LAND',
             'LOG', 'MOTHER', 'NET', 'PARTY', 'PRINCIPLE', 'RELATIVE', 'SALE',
             'SEASON', 'SIGNAL', 'SPIRIT', 'STREET', 'TREE', 'WAVE', 'BELT',
             'BENCH', 'COMMISSION', 'COPY', 'DROP', 'MINIMUM', 'PATH',
             'PROGRESS', 'PROJECT', 'SEA', 'SOUTH', 'STATUS', 'STUFF', 'TICKET',
             'TOUR', 'ANGLE', 'BLUE', 'BREAKFAST', 'CONFIDENCE', 'DAUGHTER',
             'DEGREE', 'DOCTOR', 'DOT', 'DREAM', 'DUTY', 'ESSAY', 'FATHER',
             'FEE', 'FINANCE', 'HOUR', 'JUICE', 'LIMIT', 'LUCK', 'MILK',
             'MOUTH', 'PEACE', 'PIPE', 'SEAT', 'STABLE', 'STORM', 'SUBSTANCE',
             'TEAM', 'TRICK', 'AFTERNOON', 'BAT', 'BEACH', 'BLANK', 'CATCH',
             'CHAIN', 'CONSIDERATION', 'CREAM', 'CREW', 'DETAIL', 'GOLD',
             'INTERVIEW', 'KID', 'MARK', 'MATCH', 'MISSION', 'PAIN', 'PLEASURE',
             'SCORE', 'SCREW', 'SHOP', 'SHOWER', 'SUIT', 'TONE',
             'WINDOW', 'AGENT', 'BAND', 'BLOCK', 'BONE', 'CALENDAR', 'CAP',
             'COAT', 'CONTEST', 'CORNER', 'COURT', 'CUP', 'DISTRICT', 'DOOR',
             'EAST', 'FINGER', 'GARAGE', 'GUARANTEE', 'HOLE', 'HOOK',
             'IMPLEMENT', 'LAYER', 'LECTURE', 'LIE', 'MANNER', 'MEETING',
             'NOSE', 'PARKING', 'PARTNER', 'PROFILE', 'RESPECT', 'RICE',
             'ROUTINE', 'SCHEDULE', 'SWIMMING', 'TELEPHONE', 'TIP', 'WINTER',
             'AIRLINE', 'BAG', 'BATTLE', 'BED', 'BILL', 'BOTHER', 'CAKE',
             'CODE', 'CURVE', 'DESIGNER', 'DIMENSION', 'DRESS', 'EASE',
             'EMERGENCY', 'EVENING', 'EXTENSION', 'FARM', 'FIGHT', 'GAP',
             'GRADE', 'HOLIDAY', 'HORROR', 'HORSE', 'HOST', 'HUSBAND', 'LOAN',
             'MISTAKE', 'MOUNTAIN', 'NAIL', 'NOISE', 'OCCASION', 'PACKAGE',
             'PATIENT', 'PAUSE', 'PHRASE', 'PROOF', 'RACE', 'RELIEF', 'SAND',
             'SENTENCE', 'SHOULDER', 'SMOKE', 'STOMACH', 'STRING', 'TOURIST',
             'TOWEL', 'VACATION', 'WEST', 'WHEEL', 'WINE', 'ARM', 'ASIDE',
             'ASSOCIATE', 'BET', 'BLOW', 'BORDER', 'BRANCH', 'BREAST',
             'BROTHER', 'BUDDY', 'BUNCH', 'CHIP', 'COACH', 'CROSS', 'DOCUMENT',
             'DRAFT', 'DUST', 'EXPERT', 'FLOOR', 'GOD', 'GOLF', 'HABIT', 'IRON',
             'JUDGE', 'KNIFE', 'LANDSCAPE', 'LEAGUE', 'MAIL', 'MESS', 'NATIVE',
             'OPENING', 'PARENT', 'PATTERN', 'PIN', 'POOL', 'POUND', 'REQUEST',
             'SALARY', 'SHAME', 'SHELTER', 'SHOE', 'SILVER', 'TACKLE', 'TANK',
             'TRUST', 'ASSIST', 'BAKE', 'BAR', 'BELL', 'BIKE', 'BLAME', 'BOY',
             'BRICK', 'CHAIR', 'CLOSET', 'CLUE', 'COLLAR', 'COMMENT',
             'CONFERENCE', 'DEVIL', 'DIET', 'FEAR', 'FUEL', 'GLOVE', 'JACKET',
             'LUNCH', 'MONITOR', 'MORTGAGE', 'NURSE', 'PACE', 'PANIC', 'PEAK',
             'PLANE', 'REWARD', 'ROW', 'SANDWICH', 'SHOCK', 'SPITE', 'SPRAY',
             'SURPRISE', 'TILL', 'TRANSITION', 'WEEKEND', 'WELCOME', 'YARD',
             'ALARM', 'BEND', 'BICYCLE', 'BITE', 'BLIND', 'BOTTLE', 'CABLE',
             'CANDLE', 'CLERK', 'CLOUD', 'CONCERT', 'COUNTER', 'FLOWER',
             'GRANDFATHER', 'HARM', 'KNEE', 'LAWYER', 'LEATHER', 'LOAD',
             'MIRROR', 'NECK', 'PENSION', 'PLATE', 'PURPLE', 'RUIN', 'SHIP',
             'SKIRT', 'SLICE', 'SNOW', 'SPECIALIST', 'STROKE', 'SWITCH',
             'TRASH', 'TUNE', 'ZONE', 'ANGER', 'AWARD', 'BID', 'BITTER', 'BOOT',
             'BUG', 'CAMP', 'CANDY', 'CARPET', 'CAT', 'CHAMPION', 'CHANNEL',
             'CLOCK', 'COMFORT', 'COW', 'CRACK', 'ENGINEER', 'ENTRANCE',
             'FAULT', 'GRASS', 'GUY', 'HELL', 'HIGHLIGHT', 'INCIDENT', 'ISLAND',
             'JOKE', 'JURY', 'LEG', 'LIP', 'MATE', 'MOTOR', 'NERVE', 'PASSAGE',
             'PEN', 'PRIDE', 'PRIEST', 'PRIZE', 'PROMISE', 'RESIDENT', 'RESORT',
             'RING', 'ROOF', 'ROPE', 'SAIL', 'SCHEME', 'SCRIPT', 'SOCK',
             'STATION', 'TOE', 'TOWER', 'TRUCK', 'WITNESS', 'A', 'YOU', 'IT',
             'CAN', 'WILL', 'IF', 'ONE', 'MANY', 'MOST', 'OTHER', 'USE', 'MAKE',
             'GOOD', 'LOOK', 'HELP', 'GO', 'GREAT', 'BEING', 'FEW', 'MIGHT',
             'STILL', 'PUBLIC', 'READ', 'KEEP', 'START', 'GIVE', 'HUMAN',
             'LOCAL', 'GENERAL', 'SHE', 'SPECIFIC', 'LONG', 'PLAY', 'FEEL',
             'HIGH', 'TONIGHT', 'PUT', 'COMMON', 'SET', 'CHANGE', 'SIMPLE',
             'PAST', 'BIG', 'POSSIBLE', 'PARTICULAR', 'TODAY', 'MAJOR',
             'PERSONAL', 'CURRENT', 'NATIONAL', 'CUT', 'NATURAL', 'PHYSICAL',
             'SHOW', 'TRY', 'CHECK', 'SECOND', 'CALL', 'MOVE', 'PAY', 'LET',
             'INCREASE', 'SINGLE', 'INDIVIDUAL', 'TURN', 'ASK', 'BUY', 'GUARD',
             'HOLD', 'MAIN', 'OFFER', 'POTENTIAL', 'PROFESSIONAL',
             'INTERNATIONAL', 'TRAVEL', 'COOK', 'ALTERNATIVE', 'FOLLOWING',
             'SPECIAL', 'WORKING', 'WHOLE', 'DANCE', 'EXCUSE', 'COLD',
             'COMMERCIAL', 'LOW', 'PURCHASE', 'DEAL', 'PRIMARY', 'WORTH',
             'FALL', 'NECESSARY', 'POSITIVE', 'PRODUCE', 'SEARCH', 'PRESENT',
             'SPEND', 'TALK', 'CREATIVE', 'TELL', 'COST', 'DRIVE', 'GREEN',
             'SUPPORT', 'GLAD', 'REMOVE', 'RETURN', 'RUN', 'DUE',
             'EFFECTIVE', 'MIDDLE', 'REGULAR', 'RESERVE', 'INDEPENDENT',
             'LEAVE', 'ORIGINAL', 'REACH', 'REST', 'SERVE', 'WATCH',
             'BEAUTIFUL', 'CHARGE', 'ACTIVE', 'BREAK', 'NEGATIVE', 'SAFE',
             'STAY', 'VISIT', 'VISUAL', 'AFFECT', 'COVER', 'REPORT', 'RISE',
             'WALK', 'WHITE', 'BEYOND', 'JUNIOR', 'PICK', 'UNIQUE', 'ANYTHING',
             'CLASSIC', 'FINAL', 'LIFT', 'PRIVATE', 'STOP', 'TEACH',
             'WESTERN', 'CONCERN', 'FAMILIAR', 'FLY', 'OFFICIAL', 'BROAD',
             'COMFORTABLE', 'GAIN', 'MAYBE', 'RICH', 'SAVE', 'STAND', 'YOUNG',
             'FAIL', 'HEAVY', 'HELLO', 'LEAD', 'LISTEN', 'VALUABLE', 'WORRY',
             'HANDLE', 'LEADING', 'MEET', 'RELEASE', 'SELL', 'FINISH', 'NORMAL',
             'PRESS', 'RIDE', 'SECRET', 'SPREAD', 'SPRING', 'TOUGH', 'WAIT',
             'BROWN', 'DEEP', 'DISPLAY', 'FLOW', 'HIT', 'OBJECTIVE', 'SHOOT',
             'TOUCH', 'CANCEL', 'CHEMICAL', 'CRY', 'DUMP', 'EXTREME', 'PUSH',
             'CONFLICT', 'EAT', 'FILL', 'FORMAL', 'JUMP', 'KICK', 'OPPOSITE',
             'PASS', 'PITCH', 'REMOTE', 'TOTAL', 'TREAT', 'VAST', 'ABUSE',
             'BEAT', 'BURN', 'DEPOSIT', 'PRINT', 'RAISE', 'SLEEP', 'SOMEWHERE',
             'ADVANCE', 'ANYWHERE', 'CONSIST', 'DARK', 'DOUBLE', 'DRAW',
             'EQUAL', 'HIRE', 'INTERNAL', 'JOIN', 'KILL', 'SENSITIVE',
             'TAP', 'WIN', 'ATTACK', 'CLAIM', 'CONSTANT', 'DRAG', 'DRINK',
             'GUESS', 'MINOR', 'PULL', 'RAW', 'SOFT', 'SOLID', 'WEAR', 'WEIRD',
             'WONDER', 'ANNUAL', 'COUNT', 'DEAD', 'DOUBT', 'FEED', 'FOREVER',
             'IMPRESS', 'NOBODY', 'REPEAT', 'ROUND', 'SING', 'SLIDE', 'STRIP',
             'WHEREAS', 'WISH', 'COMBINE', 'COMMAND', 'DIG', 'DIVIDE',
             'EQUIVALENT', 'HANG', 'HUNT', 'INITIAL', 'MARCH', 'MENTION',
             'SMELL', 'SPIRITUAL', 'SURVEY', 'TIE', 'ADULT', 'BRIEF', 'CRAZY',
             'ESCAPE', 'GATHER', 'HATE', 'PRIOR', 'REPAIR', 'ROUGH', 'SAD',
             'SCRATCH', 'SICK', 'STRIKE', 'EMPLOY', 'EXTERNAL', 'HURT',
             'ILLEGAL', 'LAUGH', 'LAY', 'MOBILE', 'NASTY', 'ORDINARY',
             'RESPOND', 'ROYAL', 'SENIOR', 'SPLIT', 'STRAIN', 'STRUGGLE',
             'SWIM', 'TRAIN', 'UPPER', 'WASH', 'YELLOW', 'CONVERT', 'CRASH',
             'DEPENDENT', 'FOLD', 'FUNNY', 'GRAB', 'HIDE', 'MISS', 'PERMIT',
             'QUOTE', 'RECOVER', 'RESOLVE', 'ROLL', 'SINK', 'SLIP', 'SPARE',
             'SUSPECT', 'SWEET', 'SWING', 'TWIST', 'UPSTAIRS', 'USUAL',
             'ABROAD', 'BRAVE', 'CALM', 'CONCENTRATE', 'ESTIMATE', 'GRAND',
             'MALE', 'MINE', 'PROMPT', 'QUIET', 'REFUSE', 'REGRET', 'REVEAL',
             'RUSH', 'SHAKE', 'SHIFT', 'SHINE', 'STEAL', 'SUCK', 'SURROUND',
             'ANYBODY', 'BEAR', 'BRILLIANT', 'DARE', 'DEAR', 'DELAY', 'DRUNK',
             'FEMALE', 'HURRY', 'INEVITABLE', 'INVITE', 'KISS', 'NEAT', 'POP',
             'PUNCH', 'QUIT', 'REPLY', 'REPRESENTATIVE', 'RESIST', 'RIP', 'RUB',
             'SILLY', 'SMILE', 'SPELL', 'STRETCH', 'STUPID', 'TEAR',
             'TEMPORARY', 'TOMORROW', 'WAKE', 'WRAP', 'YESTERDAY']

    def test_pogostosti_zacetnic(self):
        self.assertEqual([2, 1, 0, 1] + [0] * 21, pogostosti_zacetnic(
            ["ABRAHAM", "ANGLIJA", "BOTER", "ČEŠNJA"]))
        self.assertEqual(
            [2, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 2, 0, 2, 0, 1, 0, 0, 0, 0, 0, 0,
             0, 0, 0], pogostosti_zacetnic(self.slovar))
        self.assertEqual(
            [80, 96, 157, 8, 85, 63, 66, 46, 49, 50, 11, 12, 53, 83, 30, 26,
             142, 94, 198, 53, 81, 11, 17, 1, 7],
            pogostosti_zacetnic(self.nouns))

    def test_mozne_naslednje(self):
        mali_slovar = ["ABRAHAM", "ANGLIJA", "BOTER", "ČEŠNJA"]
        self.assertEqual(["ABRAHAM", "ANGLIJA"],
                         mozne_naslednje("ROŽA", mali_slovar))
        self.assertEqual(["BOTER"], mozne_naslednje("ROB", mali_slovar))
        self.assertEqual([], mozne_naslednje("ROBNIK", mali_slovar))

    def test_najboljsa_naslednja(self):
        self.assertEqual(
            "RDEČEKOŽEC", najboljsa_naslednja(
                ["ROB", "RDEČEKOŽEC", "RAVENA"], [0, 1, 2] + [0] * 22)
        )
        self.assertEqual(
            "RDEČEKOŽEC", najboljsa_naslednja(
                ["ROB", "RDEČEKOŽEC", "RAVENA"], [0, 2, 2] + [0] * 22)
        )
        self.assertEqual(
            "RDEČEKOŽEC", najboljsa_naslednja(
                ["RDEČEKOŽEC", "ROB", "RAVENA"], [0, 2, 2] + [0] * 22)
        )
        self.assertEqual(
            "ROB", najboljsa_naslednja(
                ["ROB", "RDEČEKOŽEC", "RAVENA"], [0, 2, 1] + [0] * 22)
        )
        self.assertEqual(
            "AZIJEC",
            najboljsa_naslednja(["AZIJEC", "ANTENA"], [1, 0, 1] + [0] * 22),
            "Si morda pozabil, da beseda sama ne šteje k pogostosti, če se začne in konča z isto črko? Beri navodila!")

    def test_sestavi_zaporedje(self):
        self.assertEqual(
            ['ABRAHAM', 'MELODIJA', 'ASTEROID', 'DREVO', 'OBLAK', 'KAČA'],
            sestavi_zaporedje(self.slovar)
        )
        self.assertEqual(
            ['LED', 'DREVORED', 'DOL', 'LES', 'SPORED', 'DROG'],
            sestavi_zaporedje(["DROG", "SPORED", "LES", "DVIG", "LED", "KOL",
                               "DREVORED", "DOL", "LOK"])
        )
        self.assertEqual(
            ['ACCESS', 'SAVINGS', 'SERIES', 'STATUS', 'STRESS', 'SUCCESS',
             'SPECIFIC', 'CLASS', 'SHIP', 'PASS', 'SHOP', 'PHYSICS', 'SLEEP',
             'POLITICS', 'SLIP', 'PRESS', 'SOUP', 'PROCESS', 'STEP', 'PROGRESS',
             'STOP', 'PANIC', 'CLOTHES', 'STRIP', 'PLASTIC', 'CROSS', 'SECTOR',
             'REPUBLIC', 'CLASSIC', 'CAMP', 'PUBLIC', 'CAP', 'POP', 'PAIR',
             'RELATIONSHIP', 'PAPER', 'RIP', 'PARTICULAR', 'RUB', 'BASIS',
             'SENIOR', 'RECOVER', 'REFRIGERATOR', 'REGISTER', 'REGULAR', 'READ',
             'DRESS', 'SHELTER', 'RECORD', 'DEEP', 'PARTNER', 'RED', 'DROP',
             'PASSENGER', 'ROOM', 'MESS', 'SAD', 'DUMP', 'PLATFORM', 'MISS',
             'SHOULDER', 'REGRET', 'TENNIS', 'SALAD', 'DAUGHTER', 'RENT',
             'THANKS', 'STORM', 'MUSIC', 'CHAMPIONSHIP', 'PERIOD', 'DEALER',
             'REPAIR', 'REPEAT', 'TOPIC', 'CHIP', 'POEM', 'MAP', 'PIZZA',
             'ADDRESS', 'SAND', 'DREAM', 'MEMBERSHIP', 'PAINT', 'TRAFFIC',
             'CUP', 'PLAYER', 'RESPOND', 'DATA', 'ANALYSIS', 'SWIM', 'MAJOR',
             'REPLACEMENT', 'TAP', 'POUND', 'DRAMA', 'AWARENESS', 'SYSTEM',
             'MANAGEMENT', 'TIP', 'POWER', 'REWARD', 'DAD', 'DEAR', 'REPORT',
             'TOP', 'PROBLEM', 'MEDIA', 'A', 'ALARM', 'MANAGER', 'REQUEST',
             'TRIP', 'PROGRAM', 'METHOD', 'DEAD', 'DEBT', 'TEA', 'ACTOR',
             'REQUIREMENT', 'TEAM', 'MANNER', 'ROAD', 'DEMAND', 'DEPARTMENT',
             'TERM', 'MANUFACTURER', 'RESIDENT', 'TEACHER', 'ROUND',
             'DEPENDENT', 'TEAR', 'RESIST', 'TOUR', 'RESORT', 'TOWER', 'RELIEF',
             'FOCUS', 'SEA', 'AREA', 'ARM', 'MAXIMUM', 'MEDIUM', 'MIND',
             'DIAMOND', 'DEPOSIT', 'TRAINER', 'RESPECT', 'TARGET', 'TABLE',
             'ECONOMICS', 'SECOND', 'DESIGNER', 'ROOF', 'FRIENDSHIP', 'PRIOR',
             'REST', 'TACKLE', 'EMPHASIS', 'SOLID', 'DINNER', 'RESTAURANT',
             'TALE', 'ENTHUSIASM', 'MINIMUM', 'MOM', 'MOOD', 'DIRECTOR',
             'RESULT', 'TASTE', 'EXAM', 'MUD', 'DISASTER', 'RIVER', 'RACE',
             'END', 'DEVELOPMENT', 'TEST', 'TELEPHONE', 'EAR', 'RAISE', 'EAST',
             'TEXT', 'TEMPERATURE', 'EDITOR', 'RANGE', 'ELEVATOR', 'RATE',
             'EAT', 'THOUGHT', 'THROAT', 'TELL', 'LOSS', 'SELF', 'FARM',
             'MASTER', 'RAW', 'WEAKNESS', 'STAFF', 'FILM', 'MATTER', 'RECIPE',
             'EMPLOYER', 'REFERENCE', 'EFFECT', 'TICKET', 'TILL', 'LEADERSHIP',
             'PROOF', 'FEED', 'DOCTOR', 'REVIEW', 'WHEREAS', 'SOUND', 'DOOR',
             'REFUSE', 'EFFORT', 'TOMORROW', 'WITNESS', 'STUFF', 'FORM', 'MAIL',
             'LIP', 'PROFESSOR', 'RELATIVE', 'EMPLOYMENT', 'TOOL', 'LAB',
             'BONUS', 'SPEED', 'DRAW', 'WRAP', 'PACE', 'ENGINEER', 'REACH',
             'HELP', 'PARENT', 'TOTAL', 'LAND', 'DRAWER', 'ROW', 'WEB', 'BOSS',
             'SPEND', 'DAMAGE', 'EARTH', 'HARM', 'MALL', 'LEAD', 'DIET',
             'TEACH', 'HALF', 'FREEDOM', 'MEMBER', 'RELEASE', 'ENTERTAINMENT',
             'TOWEL', 'LOAD', 'DRIVER', 'READING', 'GAS', 'SPREAD', 'DANCE',
             'ENVIRONMENT', 'TOOTH', 'HAND', 'DEAL', 'LAW', 'WEEKEND', 'DARE',
             'ERROR', 'RECORDING', 'GLASS', 'STAND', 'DEATH', 'HEAD', 'DETAIL',
             'LOW', 'WEIRD', 'DIRT', 'TEACHING', 'GRASS', 'STANDARD',
             'DATABASE', 'EQUAL', 'LADDER', 'RESEARCH', 'HOLD', 'DISCOUNT',
             'THEME', 'EGG', 'GUESS', 'STUPID', 'DEPTH', 'HUSBAND', 'DEVIL',
             'LAWYER', 'REMOTE', 'EQUIPMENT', 'THING', 'GAP', 'PART', 'TOUCH',
             'HAIR', 'REVEAL', 'LAYER', 'REMOVE', 'ENGINEERING', 'GROUP',
             'PAST', 'TOUGH', 'HALL', 'LEADER', 'REPRESENTATIVE', 'EQUIVALENT',
             'TRAINING', 'GRAB', 'BUS', 'SCREW', 'WIND', 'DISH', 'HELL',
             'LEATHER', 'RESERVE', 'ESTABLISHMENT', 'TRASH', 'HANG', 'GOLF',
             'FEW', 'WINDOW', 'WOOD', 'DATE', 'EXTERNAL', 'LETTER', 'RICH',
             'HABIT', 'TRAVEL', 'LEADING', 'GIRLFRIEND', 'DEBATE', 'EVENING',
             'GLAD', 'DISTRICT', 'TRUTH', 'HORROR', 'ROLL', 'LAKE', 'EVENT',
             'TIE', 'EXCITEMENT', 'TIME', 'EXIT', 'TITLE', 'EXPERT', 'TOE',
             'EXTENT', 'TONE', 'EASE', 'EDUCATION', 'NEWS', 'SHOW', 'WORD',
             'DIG', 'GOD', 'DOG', 'GOLD', 'DRAG', 'GOOD', 'DRAWING', 'GATHER',
             'ROUGH', 'HOSPITAL', 'LAUGH', 'HOUR', 'ROYAL', 'LENGTH', 'HOTEL',
             'LEVEL', 'LUNCH', 'HEALTH', 'HEARING', 'GRAND', 'DOCUMENT',
             'TONIGHT', 'TELEVISION', 'NEWSPAPER', 'RING', 'GROUND', 'DEGREE',
             'EDGE', 'ELECTION', 'NUMBER', 'RUSH', 'HIGH', 'HOUSING', 'GUARD',
             'DOT', 'TOURIST', 'TENSION', 'NAIL', 'LOCAL', 'LEG', 'GEAR',
             'RESOLVE', 'EFFECTIVE', 'EMOTION', 'NATIONAL', 'LIVING',
             'GRANDFATHER', 'RADIO', 'OFFER', 'RAIN', 'NATURAL', 'LET', 'TREAT',
             'TONGUE', 'EMPLOYEE', 'EXAMINATION', 'NORTH', 'HAT', 'TWO',
             'OFFICER', 'RATIO', 'ORDER', 'REACTION', 'NORMAL', 'LOG',
             'GRANDMOTHER', 'RESOURCE', 'ENGINE', 'EXPLANATION', 'NOVEL',
             'LONG', 'GROWTH', 'HEART', 'TRUST', 'TWIST', 'TOWN', 'NOTHING',
             'GUITAR', 'RESPONSE', 'ENTRANCE', 'EXPRESSION', 'NEAT', 'TRADE',
             'EXTENSION', 'NET', 'TRADITION', 'NIGHT', 'TREE', 'ESCAPE',
             'ESTATE', 'ESTIMATE', 'EVIDENCE', 'EXAMPLE', 'EXCHANGE', 'EXCUSE',
             'EXERCISE', 'EXPERIENCE', 'EXTREME', 'ECONOMY', 'YELLOW', 'WORLD',
             'DOUBT', 'TRAIN', 'NATION', 'NEGOTIATION', 'NECK', 'KISS', 'SNOW',
             'WASH', 'HELLO', 'OFFICIAL', 'LIFT', 'TRANSITION', 'NETWORK',
             'KEEP', 'PATH', 'HEAT', 'TRANSPORTATION', 'NAME', 'EFFICIENCY',
             'YARD', 'DRAFT', 'TURN', 'NATIVE', 'EMERGENCY', 'YEAR', 'REASON',
             'NATURE', 'EMPLOY', 'YOUTH', 'HEIGHT', 'TALK', 'KID', 'DUST',
             'TANK', 'KIND', 'DECISION', 'NEGATIVE', 'ENERGY', 'YOUNG',
             'GENERAL', 'LIGHT', 'TASK', 'KILL', 'LIMIT', 'TRACK', 'KING',
             'GIRL', 'LIST', 'TRICK', 'KITCHEN', 'NERVE', 'ENTRY', 'YOU',
             'UPSTAIRS', 'SURROUND', 'DEFINITION', 'NOISE', 'ESSAY',
             'YESTERDAY'],
            sestavi_zaporedje(self.nouns))


if __name__ == "__main__":
    unittest.main()
