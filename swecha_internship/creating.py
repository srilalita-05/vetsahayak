import pandas as pd
# Expanded FAQs for each animal (10 questions each)
expanded_species_faqs = {
    "Dog": [
        ("How often should I vaccinate my dog?", "Dogs need core vaccines such as rabies, distemper, parvovirus, and hepatitis. Boosters are required every 1–3 years depending on local regulations and vet advice."),
        ("What foods are toxic to dogs?", "Chocolate, onions, garlic, grapes, raisins, xylitol, alcohol, and cooked bones are toxic to dogs."),
        ("How often should I deworm my dog?", "Puppies should be dewormed every 2–3 weeks until 12 weeks of age, then monthly until 6 months, and at least every 3–6 months as adults."),
        ("How do I know if my dog has fleas?", "Excessive scratching, hair loss, visible tiny black specks (flea dirt), and irritated skin may indicate fleas."),
        ("How can I prevent heatstroke in dogs?", "Provide shade, fresh water, avoid exercise in hot weather, and never leave dogs in cars."),
        ("How often should I bathe my dog?", "Every 4–6 weeks is sufficient for most dogs, but frequency depends on coat type and lifestyle."),
        ("How much exercise does my dog need?", "Most dogs need 30 minutes to 2 hours of exercise daily, depending on age and breed."),
        ("Can I give my dog human medicine?", "No. Many human medicines are toxic to dogs. Always consult a veterinarian first."),
        ("How can I tell if my dog is overweight?", "If you cannot feel your dog's ribs easily and they lack a defined waist, they may be overweight."),
        ("What are emergency signs in dogs?", "Difficulty breathing, persistent vomiting, seizures, inability to stand, and uncontrolled bleeding require urgent veterinary care.")
    ],
    "Cat": [
        ("How often should I vaccinate my cat?", "Cats require core vaccines like feline distemper, calicivirus, rhinotracheitis, and rabies. Boosters are given every 1–3 years."),
        ("What foods are toxic to cats?", "Onions, garlic, chocolate, grapes, raisins, alcohol, caffeine, and bones are toxic to cats."),
        ("Should cats stay indoors?", "Indoor cats generally live longer and are safer from accidents, diseases, and predators."),
        ("How often should I deworm my cat?", "Kittens should be dewormed every 2 weeks until 12 weeks old, then monthly until 6 months, and at least every 3–6 months as adults."),
        ("How do I prevent hairballs in cats?", "Regular grooming and special hairball-control diets can help reduce hairballs."),
        ("How often should I groom my cat?", "Short-haired cats need brushing weekly, while long-haired cats may need daily brushing."),
        ("Can I feed milk to my cat?", "Most adult cats are lactose intolerant. Avoid cow’s milk and provide fresh water instead."),
        ("What are signs of illness in cats?", "Loss of appetite, lethargy, hiding, vomiting, diarrhea, and respiratory issues are warning signs."),
        ("How do I know if my cat is stressed?", "Stress signs include hiding, over-grooming, aggression, and changes in litter box use."),
        ("What are emergency signs in cats?", "Difficulty breathing, sudden collapse, persistent vomiting, seizures, and inability to urinate are emergencies.")
    ],
    "Cow": [
        ("How often should cows be vaccinated?", "Cows need vaccinations against foot-and-mouth disease, brucellosis, black quarter, and hemorrhagic septicemia, as advised by the vet."),
        ("What is mastitis in cows?", "Mastitis is an udder infection causing swelling, heat, redness, clots in milk, and reduced yield."),
        ("What should cows eat daily?", "Cows need a diet of green fodder, dry fodder, concentrates, and clean drinking water."),
        ("How can I improve milk yield in cows?", "Provide balanced nutrition, regular health checks, and stress-free milking practices."),
        ("How often should cows be dewormed?", "Cows should be dewormed every 3–6 months depending on grazing conditions."),
        ("What are signs of bloat in cows?", "Distended left abdomen, discomfort, restlessness, and difficulty breathing are signs of bloat."),
        ("How can I prevent foot-and-mouth disease?", "Follow vaccination schedules and maintain good farm hygiene to reduce risk."),
        ("What is the normal temperature of a cow?", "The normal rectal temperature of a cow is 101.5°F (38.6°C)."),
        ("What are common cow diseases?", "Common diseases include mastitis, brucellosis, foot-and-mouth, anthrax, and black quarter."),
        ("What are emergency signs in cows?", "Difficulty standing, collapse, inability to eat or drink, and severe breathing problems require immediate vet care.")
    ],
    "Cattle": [
        ("What is the difference between cattle and cow?", "Cow refers specifically to female bovines, while cattle is a general term for all domesticated bovines including bulls, cows, and calves."),
        ("How often should cattle be vaccinated?", "Vaccination schedules vary but generally include vaccines against FMD, brucellosis, black quarter, and HS as advised by local vets."),
        ("What should be the housing for cattle?", "Cattle need clean, dry, and well-ventilated sheds with enough space for movement."),
        ("How do I detect lameness in cattle?", "Signs include limping, reluctance to move, swelling in hooves or joints."),
        ("How often should cattle be fed?", "Cattle should be fed 2–3 times a day with adequate fodder and water."),
        ("What are signs of heat in cattle?", "Restlessness, bellowing, reduced appetite, and mounting other cattle indicate heat."),
        ("How much water do cattle need daily?", "Adult cattle need 30–50 liters of clean water daily depending on climate and diet."),
        ("How can I prevent tick infestations?", "Use acaricides, maintain hygiene, and rotate grazing pastures."),
        ("What are signs of brucellosis in cattle?", "Abortions, reduced fertility, and retained placenta are signs of brucellosis."),
        ("What are emergency signs in cattle?", "Severe bloat, sudden collapse, inability to stand, and uncontrolled bleeding require emergency vet care.")
    ],
    "Buffaloes": [
        ("How often should buffaloes be vaccinated?", "Buffaloes need vaccination against diseases like FMD, HS, BQ, and brucellosis as per vet advice."),
        ("What is the average milk yield of buffaloes?", "Milk yield varies by breed but typically ranges between 4–12 liters per day."),
        ("What should buffaloes eat?", "Buffaloes thrive on green fodder, crop residues, dry fodder, and concentrates with ample water."),
        ("How do I prevent mastitis in buffaloes?", "Maintain udder hygiene, clean housing, and proper milking techniques."),
        ("How often should buffaloes be dewormed?", "Every 3–6 months depending on grazing conditions."),
        ("What is the normal temperature of buffaloes?", "The normal rectal temperature of buffaloes is around 100.5–102.5°F (38–39°C)."),
        ("How can I improve milk quality in buffaloes?", "Provide balanced feed, mineral supplements, clean water, and reduce stress."),
        ("How can I prevent bloat in buffaloes?", "Avoid sudden changes in diet, provide roughage, and prevent overeating of legumes."),
        ("What are common diseases in buffaloes?", "Mastitis, HS, FMD, brucellosis, and parasitic infestations are common diseases."),
        ("What are emergency signs in buffaloes?", "Inability to rise, severe bloating, persistent diarrhea, and breathing difficulty need urgent vet attention.")
    ],
    "Chicken": [
        ("How often should chickens be vaccinated?", "Chickens should be vaccinated against Marek’s disease, Newcastle disease, and infectious bronchitis as per poultry schedule."),
        ("What should chickens eat?", "Balanced poultry feed with grains, protein, vitamins, minerals, and clean water."),
        ("What are signs of Newcastle disease?", "Coughing, sneezing, twisted neck, paralysis, and sudden death are signs of Newcastle disease."),
        ("How can I prevent egg drop in chickens?", "Provide adequate nutrition, calcium supplements, and vaccination."),
        ("How much space do chickens need?", "Each chicken should have at least 1.5–2 square feet of floor space in coops."),
        ("What are signs of coccidiosis in chickens?", "Bloody diarrhea, lethargy, poor appetite, and weight loss indicate coccidiosis."),
        ("How can I prevent parasites in chickens?", "Keep litter dry, rotate grazing, and use deworming medicines as recommended."),
        ("What is the normal lifespan of a chicken?", "Backyard chickens can live 6–8 years with good care."),
        ("How often do hens lay eggs?", "Healthy hens lay 4–6 eggs per week depending on breed and season."),
        ("What are emergency signs in chickens?", "Sudden drop in egg production, respiratory distress, and inability to stand require urgent vet care.")
    ],
    "Birds": [
        ("What should pet birds eat?", "A mix of seeds, fresh fruits, vegetables, and pellets. Avoid avocado, chocolate, caffeine, and alcohol."),
        ("How often should bird cages be cleaned?", "Daily cleaning of food and water dishes, and weekly cleaning of the cage is recommended."),
        ("Can birds be vaccinated?", "Yes, some birds require vaccines against diseases like Newcastle disease and polyomavirus, depending on species and region."),
        ("How do I know if my bird is sick?", "Signs include feather fluffing, loss of appetite, drooping wings, labored breathing, and quiet behavior."),
        ("Do birds need company?", "Most birds are social and benefit from companionship or regular human interaction."),
        ("How often should I take my bird to the vet?", "At least once a year for a health checkup, and more often if showing illness signs."),
        ("Can birds talk?", "Some species like parrots and mynahs can mimic human speech with training."),
        ("How do I prevent feather plucking?", "Provide enrichment, reduce stress, ensure proper diet, and seek vet help if persistent."),
        ("What temperature is safe for birds?", "Most pet birds are comfortable between 65–80°F (18–27°C). Avoid sudden temperature changes."),
        ("What are emergency signs in birds?", "Difficulty breathing, seizures, bleeding, sudden inability to perch, or not eating require urgent vet care.")
    ],
    "Deer": [
        ("What do deer eat?", "Deer mainly eat grasses, leaves, shoots, fruits, and nuts depending on season."),
        ("Do deer need salt licks?", "Yes, salt and mineral licks help provide essential minerals in their diet."),
        ("What are common deer diseases?", "Deer can suffer from chronic wasting disease, bluetongue, and parasitic infestations."),
        ("Can deer be domesticated?", "Deer are wild animals and cannot be fully domesticated, but they can be farmed in controlled environments."),
        ("How do I prevent disease spread in deer?", "Maintain clean enclosures, avoid overcrowding, and follow vaccination/deworming schedules advised by wildlife vets."),
        ("What is the lifespan of a deer?", "Deer can live 10–20 years depending on species and environment."),
        ("How do deer communicate?", "Deer communicate using body language, vocal calls, and scent marking."),
        ("What should I do if I find an injured deer?", "Contact local wildlife authorities or a vet trained in wildlife care. Do not attempt treatment yourself."),
        ("Are deer dangerous?", "Deer are generally shy, but can be dangerous if cornered, especially males during rutting season."),
        ("What are emergency signs in deer?", "Severe injury, inability to stand, bleeding, or neurological signs require immediate wildlife vet attention.")
    ],
    "Black-tailed Deer": [
        ("Where do black-tailed deer live?", "They are native to the western coastal regions of North America, living in forests and meadows."),
        ("What do black-tailed deer eat?", "They eat grasses, shrubs, berries, acorns, and agricultural crops."),
        ("What predators hunt black-tailed deer?", "Predators include mountain lions, wolves, coyotes, and bears."),
        ("What are common diseases in black-tailed deer?", "They may be affected by chronic wasting disease, parasites, and bacterial infections."),
        ("How long do black-tailed deer live?", "In the wild, they live about 8–12 years; in captivity, they may live longer."),
        ("When do black-tailed deer breed?", "They breed in fall (November–December) with fawns born in spring."),
        ("What is the normal behavior of black-tailed deer?", "They are crepuscular, most active at dawn and dusk, and live in small groups."),
        ("Are black-tailed deer dangerous?", "They are generally shy but males can be aggressive during rutting season."),
        ("How can black-tailed deer be protected?", "Conservation includes habitat preservation, regulated hunting, and disease monitoring."),
        ("What are emergency signs in black-tailed deer?", "Injury, neurological symptoms, or inability to stand should be reported to wildlife authorities.")
    ]
}

# Build dataset with all animals and FAQs
expanded_faq_data = []
for animal, faqs in expanded_species_faqs.items():
    for q, a in faqs:
        expanded_faq_data.append({"Animal": animal, "Question": q, "Answer": a})

expanded_faq_df = pd.DataFrame(expanded_faq_data)

# Save to CSV
expanded_faq_file_path = "D:\\swecha_internship\\all_animals_faqs.csv"
expanded_faq_df.to_csv(expanded_faq_file_path, index=False)

expanded_faq_file_path
