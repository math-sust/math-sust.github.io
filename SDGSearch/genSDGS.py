import csv


courses = open("SustainCourses.tsv","r")
reader = csv.reader(courses, delimiter='\t')



pastIQPsdgKeywords = [["Developing Countries", "Economic Resources", "Equality", "Financial Inclusion",
    "Income Equality", "Inequality", "Overuse Of Resource", "Poverty", "Quality Of Life", "Resource Efficiency",
    "Resource Overuse", "Third World", "Vulnerable", "Wealth Distribution", "Impoverished", "Poverty Reduction"],

    ["Consumption of Resources", "Food Gap",
        "Food Reserves", "Food Security", "Hunger", "Hungry People", "Malnutrition", "Nutrition", "Resource Consumption",
        "Rural Infrastructure", "Sustainable Agriculture"],

    ["Air Contamination", "Air Pollution", "Child Deaths", "Clean Water",
        "Disability", "Healthy Living", "International Health Policy", "International Health Regulations", "Reducing Malaria",
        "Reducing Mortality", "Soil Contamination", "Soil Pollution", "Treatment Of Substance Abuse", "Well Being", "Wellbeing",
        "Well-Being", "Active Lifestyle", "Adolescent Development", "Baby Development", "Child Development", "Mental Health", "Sustainable Livelihood"],

    ["Access To Education", "Basic Literacy", "Equal Education", "Equitable Education", "Gender Disparities In Education",
        "Gender Disparity", "Gender Equality", "Gender Equity", "Gender Sensitive", "Inclusive Education", "Opportunities For All",
        "Refugees And Learning", "Universal Education", "Education Sector", "Special Education", "Sustainable Education"],

    ["Disadvantaged", "Discrimination", "Empower women", "Empowering Girls",
        "Empowering Women", "Empowerment Of Girls", "Empowerment Of Women", "Equal Access", "Exploitation", "Female Empowerment",
        "Female Genital Mutilation", "Feminism", "Forced Marriage", "Gender Discrimination", "Gender equality", "Human Rights",
        "Human Trafficking", "Humanitarian", "Marginalised", "Reproductive Health", "Reproductive Rights", "Sexual Health", "Sexual Violence", "Social Inclusion", 
        "Unemployment", "Universal Health Coverage", "Violence Against Girls", 
        "Violence Against Women",
        "Women Empowerment", "Women's Rights", 
        "Workplace Equality", "Women equality", "Women Rights"],

    ["Accessible Water", "Affordable Drinking Water", "Contaminated",
        "Contamination", "Ecosystem Protection", "Ecosystem Restoration", "Equitable Sanitation", "Hydropower", "Improving Water",
        "Inadequate Water", "Pollution", "Recycle", "Safe Drinking Water", "Sanitation", "Water Access", "Water Disasters",
        "Water Ecosystems", "Water Efficiency", "Water Harvesting", "Water Quality", "Water Resources Management", "Water Scarcity",
        "Water Supply", "Water-related Ecosystems", "Water-use Efficiency"],

    ["Affordable Energy", "Alternative Energy", "Fossil Fuel",
        "Fossil-fuel", "Green Economy", "Greenhouse Gas", "Greenhouse Gas Emissions", "Hydroelectric", "Low Carbon", "Reliable Energy",
        "Renewable", "Solar Energy", "Solar Power", "Sustainable Energy", "Wave Energy", "Wave Power", "Wind Energy", "Wind Power", "Energy Efficiency"],

    ["Decent Work", "Economic growth", "Equal Pay", "Global Resource Efficiency", "Productive employment", "Sustainable Economic Growth",
        "Sustainable Growth", "Economic Instability", "Economic Sustainability", "Equal Rights to Economic Resource"],

    ["Foster innovation", "Infrastructure", "Resilient Infrastructure", "Resource Use Efficiency",
        "Sustainable Industrialization", "Water Resources"],

    ["Ageism", "Discriminatory", "Equal Opportunity", "Racism", "Reduce Inequality",
        "Sexism", "Classism", "Human Rights", "Inclusion", "Marginalization", "Segregation", "Social Inclusion"],

    ["Air Quality", "Climate Change", "Disaster Management", "Disaster Risk Reduction", "Human settlements",
        "Inadequate Housing", "Inclusive Cities", "Inclusive human Settlements", "Land Consumption", "Resource Needs", "Smart Cities",
        "Waste Generation", "Waste Management", "Habitat Quality"],

    ["Decarbonisation", "Efficient Use Of Resources", "Energy Consumption", "Energy Efficiency",
        "Energy Use", "Food Losses", "Food Supply", "Food Waste", "Future Proof", "Greenhouse Gasses", "Natural Resources",
        "Productive Patterns", "Recycling", "Reduce Waste Generation", "Reduction", "Sustainable Consumption", "Water Pollution", "Alternative Energy",
        "Consumption of Fossil Fuels", "Consumption of Natural Resource", "Consumption of Resource", "Recycling", "Resource Management"],

    ["Climate Action", "Climate change", "Climate Change Planning", "Climate Change Policy", "Cop 21", "Cop 22", "Emissions",
            "Extreme Weather", "Global Mean Temperature", "Global Temperature", "Global Warming", "Greenhouse Gases", "Ice Loss",
            "Low-carbon Economy", "Ocean Systems", "Paris Agreement", "Rising Sea", "Sea Level Rise", "Natural Hazards", "Pollution"],

    ["Conservation", "Conserve",
            "Conserve Oceans", "Ecosystem Management", "Marine", "Ocean Acidification", "Ocean Temperature", "Oceans", "Protected Areas",
            "Seas", "Sustainable Oceans", "Vulnerable Species"],

    ["Biodiversity", "Deforestation", "Desertification", "Desertifications", "Ecosystems",
            "Illegal Wildlife Products", "Land Conservation", "Land Degradation", "Land Loss", "Land Use And Sustainability", "Manage Forests",
            "Protected Fauna", "Protected Flora", "Protected Species", "Reforestation", "Soil Degradation", "Terrestrial Ecosystems",
            "Threatened Species", "Ecological System", "Enabling Environment", "Environmental Assessment", "Environmental Degradation",
            "Environmental Issue", "Environmental Sustainability", "Environmentally Sensitive", "Environmentally-Sensitive", "Land use",
            "Natural Environment"],

    ["Access to Justice", "Accountable Institutions", "Hate Crime", "Inclusive Institutions", "Inclusive Societies",
            "Peace", "Peaceful Societies", "Justice Legislation", "Justice Sector", "Safe Communities", "Supporting Families"],

    ["Doha Development Agenda", "Environmentally Sound Technologies", "Global Partnership",
            "Global Partnerships For Sustainable Development", "International Cooperation", "International Support", "Poverty Eradication",
            "Sustainability", "Sustainable", "Women Entrepreneurs", "Future Policy", "SDG", "Social Sustainability", "Sustainable Development",
            "Environmental Policy"]]

cleanedWords = []
for sdg in pastIQPsdgKeywords:
    words = []
    for word in sdg:
        words.append(word.lower())
    cleanedWords.append(words)


for row in reader:
        title = row[2].lower()
        desc = row[4].lower()
        sdgs = []
        for x in range(0,17):
            sdg = cleanedWords[x]
            for word in sdg:
                if(word in title or word in desc):
                    sdgs.append(x+1)
                    
                    break
        print(sdgs)





