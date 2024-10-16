import discord
import random
import asyncio
from discord.ext import commands
from model import get_class

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)
bot.remove_command("help")

#Information
enlacesCC = ["https://www.un.org/es/climatechange/what-is-climate-change", "https://www.un.org/es/climatechange/science/causes-effects-climate-change", "https://www.enelgreenpower.com/es/learning-hub/transicion-energetica/cambio-climatico-causas-consecuencias", "https://www.iberdrola.com/sostenibilidad/isla-de-plastico-pacifico-septimo-continente", "https://www.fundacionaquae.org/wiki/alarmante-aumento-de-la-isla-de-basura/", "https://www.iberdrola.com/sostenibilidad/las-5-islas-de-basura-en-el-mundo", "https://en.wikipedia.org/wiki/Great_Pacific_garbage_patch", "https://theoceancleanup.com/", "https://thesustainableinnovator.com/solarpunk-a-blueprint-for-a-sustainable-world-worth-living-in-1a88eb065330", "https://en.wikipedia.org/wiki/Solarpunk", "https://en.wikipedia.org/wiki/Solarpunk", "https://www.bbc.com/news/business-57761297", "https://thebulletin.org/doomsday-clock/"]
enlacesIE = ["https://forodiplomatico.com/cinco-avances-tecnologicos-medioambiente/", "https://www.solarreviews.com/blog/how-are-solar-panels-made", "https://www.energy.gov/eere/solar/solar-photovoltaic-manufacturing-basics", "https://www.bbc.com/news/technology-64744926", "https://www.sailworldcruising.com/news/279084/The-GPGP-can-be-cleaned-for-USD75-billion", "https://plasticseurope.org/plastics-explained/a-large-family/biodegradable-plastics/", "https://en.wikipedia.org/wiki/Biodegradable_plastic", "https://www.nationalgeographic.com/science/article/bioplastic-biodegradable-compostable-plastic-pha", "https://www.certifiedenergy.com.au/emerging-materials/emerging-materials-mycelium-brick", "https://www.biobasedpress.eu/2020/04/mycelium-as-a-construction-material/"]
CCquestions = {"To which country is the Garbage Island compared to?" : "France", "What's the main material that solar panels made of?" : "Silicon", "When is Earth day celebrated?" : "April 22", "What year was Earth Day first held?" : "1970", "How far from midnight is the Doomsday Clock at?" : "90 seconds", "What year was the Doomsday Clock created?" : "1947", "When was the hand of the Doomsday Clock furthest from midnight?" : "1991"}
funfacts = ["Did you know Dolphins have names for eachother? Research has found that the sounds dolphins make when calling out to friends or family are specific to the member being called!", "Did you know that trees communicate with eachother? Through their system of roots they can communicate, and if one tree is in need of nutrients the ones surrounding will give them the nutrients they can spare so the weaker one keeps growing.", "Did you know buffaloes make decisions by voting? Research has found that when making decisions as a group, african buffaloes don't simply listen to their leader, they actually vote on what to do.", "Did you know that there are more trees on Earth that stars in our galaxy? Up to 12 times more!", "Did you know the Earth isn't actually round? Although it is technically spherical, due to all the changes in terrain and a slight stretching at the equator, it is actually a geoid.", "Did you know that coral reefs are alive? Although they may just look like strange colorful structures, they are living beings and in fact, they are the largest living being in the planet", "Did you know that Australia is technically wider than the moon? While the moon is roughly 3400km in diameter, Australia is 4000km wide from east to west."]
#--

#Flower Tips
PoppyTips = ["Poppy grows best in full sun and requires well-drained, fertile soil.", " Sow seeds in early spring in rows 12 to 24 inches apart and cover with 1/8 inch of soil.", "Keep the seed bed moist until plants emerge, it can take from 7 to 28 days."]
CamelliaTips = ["Plant in autumn or spring.", "It needs an acid-type of soil.", "Most species prefer the shade.", "You can grow it in containers if need be."]
NasturtiumTips = ["Plant nasturtiums in well-drained soil in full sun.", "Plant in late spring to early summer if you want to keep it in your garden.", "Space them 30-45cm apart.", "They make good companions plants to brassicas and chard."]
MarigoldTips = ["They are easily grown in full sun.", "They need moderately fertile, dry to moist, well-drained soils.", "Tall varieties should be planted in locations sheltered from strong winds and heavy rains."]
CarnationTips = ["Carnations prefer full sun.", "They prefer slightly alkaline soil that is well-drained.", "Keep moist at all times and place in a warm position."]
ChrysantemumTips = ["Grow in moist but well-drained soil with added compost.", "They need a sheltered but sunny spot.", "All chrysanthemums need staking."]
SunflowerTips = ["Plant sunflower seeds 1 to 2 inches deep after the last threat of frost.", "Space the seeds around 6 inches apart.", "They grow in three or four months and can get up to 12 feet tall.", "Plant in a spot that gets a lot of sun."]
HydrangeaTips = ["Hydrangeas do best in fairly moist soil.", "Water the plant well an hour or so before you plant it.", "Never plant a hydrangea deeper than it was in its original pot.", "They love water, so keep it watered everyday.", "Plant in a place with sunny mornings and shady afternoons."]
JasmineTips = ["They need moist but free-draining soil in full sun.", "You should plant them with a trellis, they need support.", "Cut back after flowering.", "Feed weekly with a high potash fertiliser."]
LilyTips = ["They are best grown in morning sun, or light shade.", "Liliums like humus rich, moist and acid soil.", "You should keep them protected from the heat, they don't like to be dry."]
DaisyTips = ["They do best in full sun.", "Cover the sowed seeds with an eighth of an inch of soil so that the sunlight can still reach the seeds.", "Plant the seeds in nutrient-rich, well-draining soil."]
NarcissusTips = ["Dig a hole at least twice the length of the bulb deep.", "Plant at least 10cm apart.", "Plant in a sunny or lightly shaded area with freely draining soil.", ""]
OrchidTips = ["They like bright light but not the direct sun.", "They like regular watering and misting, preferably with rainwater (or boiled and cooled).", "Many need to be grown in bark-based orchid compost."]
PassionflowerTips = ["They will grow anywhere as long as they get a lot of sun.", "Fertilize in early spring", "You should water 3 or 4 times a week until it has grown enough, as it's more tolerant to drought."]
PeonyTips = ["Plant in full sun and a fertile soil.", "They will grow in mostly any soil, as long as they don't dry out or get waterlogged.", "They don't need any winter protection."]
PetuniaTips = ["They need plenty of sun, a fertile soil, and shelter from strong winds.", "They are very versatile plants and adapt well to any container.", "They need fertile but well-drained soil."]
RoseTips = ["Roses require at least 6 hours of full sun a day (preferably in the morning).", "They need a well-drained and nutrient-rich soil, and moderate amounts of water.", "Water should only be applied directly to the root zone."]
TulipTips = ["They are best planted in the fall after soils have cooled off.", "They need very fertile soil.", "They prefer non-direct sunlight with some shade."]
#--

#Fruit Tips
BananaTips = ["Grow banana plants in full sun to partial shade.", "Mulch the roots and protect the stem.", "Fresh seeds should germinate quickly, while older seeds may take up to six months."]
CherryTips = ["Cherry trees do best in a warm, sheltered frost-free spot.", "They prefer well-drained, slightly acid soil.", "Depending on the species, they need to be spaced from 6 to 25 feet apart."]
ApricotTips = ["Stake your tree in windy climates.", "Prune every year to remove dead or diseased branches.", "Harvest in mid- to late summer.", "Fertilize in late winter and late summer."]
FigTips = ["Figs need a warm, sunny, sheltered spot to crop well.", "Spring is the ideal time to plant, so they have a full growing season to get established.", "plant into a hole lined with paving slabs or into a large container sunk into the ground or free-standing."]
KiwiTips = ["The vines need plenty of sunlight and shelter to survive.", "They require a fertile, well-drained, acidic soil.", "They can grow up to 26 feet."]
LimeTips = ["They require full sun to produce the best fruit.", "They mostly prefer neutral soil.", "Mulching around the base of the tree can assist in retaining moisture and regulating temperature."]
LemonTips = ["Give your lemon tree plenty of bright light, it loves soaking up the sun.", "Water when the top two inches of soil feel dry, and check regularly in summer.", "Feed your lemon tree with nutrients once a month in spring and summer for more fruit."]
MangoTips = ["Mango trees need a frost free, sunny position where the soil is well drained.", "Place them in a spot where they'll also be protected from cold winter wind and rain.", "Put a generous amount of compost over an area of about 1.5-2m wide."]
AppleTips = ["Choose a planting site with fertile soil that drains freely and doesn't become waterlogged.", "Apple trees like full sun and a warm sheltered site.", "Try to keep the plants cool during hot summers, their max temperature is 35C"]
PassionFruitTips = ["Plant your passion fruit in moist, well-draining soil.", "Water generously as they do love water when young.", "Plant where it can get the most sunlight.", "Propagate your plant with cuttings."]
OrangeTips = ["They can grow in mostly any kind of soil.", "Orange plants need to be watered to grow well, especially in the beginning.", "Weed them out well as they're prone to get damaged."]
AvocadoTips = ["Place the plant where it can get most sunlight.", "They prefer acidic and loamy soil.", "They prefer infrequent but deep watering, so when watering do give them a lot of it.", "As a tropical plant, they prefer high temperatures between 50F and 85F."]
PearTips = ["Soil should be slightly acidic.", "Soil should be well-drained, water does not stand for long after a rain.", "Plant in full sun away from structures or other trees."]
GrapefruitTips = ["Choose a sunny spot with well drained soil.", "Mulch around the base with organic mulch like woodchip or pea straw, keeping it away from the trunk.", "Water your tree regularly and prune it during the spring."]
#--

#Veggie Tips
EggplantTips = ["Choose an area with abundant sunlight.", "It needs fertile, well-drained soil.", "Keep soil moist but not soggy.", "Keep your plants fed by feeding them regularly with a continuous-release plant food."]
BroccoliTips = ["Broccoli should be planted in a site that gets full sun.", "The soil should be slightly acidic.", "It's best to plant in early spring as it prefers colder climates."]
OnionTips = ["Grow them in a sunny spot that has fertile, well-drained soil.", "The soil must be slightly acidic.", "You can put the roots in a water cup until they start growing, then place in the soil."]
CauliflowerTips = ["Cauliflower should be grown in a spot that gets full sun.", "Cauliflower grows best as a fall crop.", "It's best to use seedlings than an actual seed."]
SpinachTips = ["Spinach is a cool-season vegetable.", "It prefers sunny locations and fertile, well-drained soil.", "Plant seeds ½ inch deep, 2-3 weeks before the last frost in the spring."]
PeasTips = ["Sow seeds 4 to 6 weeks before the last spring frost date when the soil is cool", "Select a sunny location and well-draining soil.", "Snow will not hurt emerging pea plants but try to keep them in temperatures between 15C and 25C"]
LettuceTips = ["Lettuce is a cool-season vegetable.", "It prefers sunny locations and fertile, well-drained soil.", "Plant seeds ¼-½ inch deep, 2-3 weeks before the last frost."]
ChiliTips = ["Sow from January to March.", "Place seeds in warm water for several hours before sowing.", "During germination, temperatures of at least 20°C and a bright location are crucial.", "Keep soil moist."]
TurnipTips = ["Sow seeds directly in the garden 10mm deep and 7-15cm apart, with rows 20-40cm apart.", "Keep soil moist but never wet or dry.", "Turnips require full sun and fertile soil."]
PotatoTips = ["Dig a trench 15cm (6in) deep, place the seed potatoes along the base with the sprouts upwards.", "You should plant them in spring for best results.", "When the shoots reach 20cm tall, use a rake, hoe or spade to mound soil up around the bases of the shoots, covering the stems half way."]
CucumberTips = ["Cucumbers thrive when the weather is hot and water is plentiful.", "IF the plant is a vine, it will need a trellis.", "Plant cucumbers when average daily temperatures reach the mid-70s° F.", "Cucumbers will grow quickly with little care. Be sure they receive an inch of water every week."]
BeetTips = ["Beets are cool season vegetables that prefer sunny locations and fertile, deep, well-drained soils.", "Plant seeds ¼-½ inch deep. Thin seedling beets to 3 inches apart in the row with rows 12-18 inches apart.", "Incorporate plenty of organic matter and a complete fertilizer into the area before planting."]
CabbageTips = ["Plant seeds ¼-½ inch deep, 2-3 weeks before the last frost in the spring.", "Thin seedlings or transplant cabbage 12-18 inches apart in the row with rows 2-3 feet apart.", "Avoid fertilization during head formation as this causes excessive leaf growth and head splitting.", "Irrigation should be deep and infrequent."]
TomatoTips = ["Tomatoes thrive in rich, free-draining but moisture-retentive soil", "Choose your warmest, sunniest spot, sheltered from wind.", "Space plants 45 to 60cm (18 to 24in) apart, depending on their eventual size, check seed packets for exact spacings."]
CarrotTips = ["Carrots are cool season vegetables that prefer sunny locations and fertile, deep, well-drained soils.", "Incorporate plenty of organic matter and a complete fertilizer into the area before planting.", "Plant seeds ¼-½ inch deep. Thin seedling carrots to 3 inches apart in the row with rows 12-18 inches apart."]
PumpkinTips = ["Do not sow seeds directly until well after the danger of frost is past.", "Soil needs temperatures between 65° and 95°F", "Where the growing season is very short, start by sowing indoors in peat pots, 2 to 4 weeks before the last spring frost."]
#--

#Commands and Events
@bot.event
async def on_ready():
    print (f" Se inició el bot {bot.user}")

@bot.command()
async def hello(ctx):
    username = ctx.message.author.mention
    await ctx.send("Hello there, " + username + ". I am the Climate Change Boty! You can use '!help' to view my commands.")

@bot.command()
async def help(ctx):
    embed = discord.Embed(title= "Help Command!", description= "This command displays all the available commands to use with this bot! Enjoy learning!", color= 0x68e32f )
    embed.add_field(name= "!hello", value= "This command is to say hello to the bot!", inline= False)
    embed.add_field(name= "!cchange", value= "This command will give you a random url about the effects of Climate Change!", inline= False)
    embed.add_field(name= "!electricinn", value= "This command will give you a random url about innovations to help with Climate Change!", inline= False)
    embed.add_field(name= "!facts", value= "This command will give you a random facts to help keep a clean, environment-friendly space!", inline= False)
    embed.add_field(name= "!questionaire", value= "This command will start a round of Questionaire! You'll be given a question about the environment and you'll have to answer in under 120 seconds.", inline= False)
    embed.add_field(name="!checkflower", value="This is an image recognition AI, you must send an image of a flower and it will recognise it, then give you tips to plant it in your garden!", inline= False)
    embed.add_field(name="!checkfruit", value="This is an image recognition AI, you must send an image of a fruit and it will recognise it, then give you tips to plant it in your garden!", inline= False)
    embed.add_field(name="!checkveggie", value="This is an image recognition AI, you must send an image of a vegetable and it will recognise it, then give you tips to plant it in your garden!", inline= False)
    await ctx.send(embed=embed)

@bot.command()
async def cchange(ctx):
    embed = discord.Embed(title= "New Website Link!")
    embed.add_field(name= "This is a link about Climate Change, and a warning.", value="", inline= False)
    embed.add_field(name= random.choice(enlacesCC), value="", inline= False)
    await ctx.send(embed = embed)

@bot.command() 
async def electricinn(ctx):
    embed = discord.Embed(title= "New Website Link!")
    embed.add_field(name= "This is a link about Enviromental Innovations, we still have time.", value= "", inline= False)
    embed.add_field(name= random.choice(enlacesIE), value="", inline= False)
    await ctx.send(embed = embed)

@bot.command()
async def facts(ctx):
    embed = discord.Embed(title= "Fun Facts!")
    embed.add_field(name= "This is a Fun Fact! Nature can be beautiful and interesting.", value="", inline= False)
    embed.add_field(name= random.choice(funfacts), value="", inline= False)
    await ctx.send(embed = embed)

@bot.command()
async def questionaire(ctx):
    await ctx.send("Do you want to play a round of Questionaire? (y/n)")
    def check(m: discord.Message):  # m = discord.Message.
        return m.author.id == ctx.author.id and m.channel.id == ctx.channel.id
    
    try:
        #              event = on_message without on_
        msg = await bot.wait_for('message', check = check, timeout = 60.0)
        # msg = discord.Message
    except asyncio.TimeoutError: 
        # at this point, the check didn't become True, let's handle it.
        await ctx.send(f"**{ctx.author}**, you didn't send any message in the time limit :(")
        return
    else:
        # at this point, the check has become True and the wait_for has done its work, now we can do ours.
        # we could also do things based on the message content here, like so
        # if msg.content == "this is cool":
        #    return await ctx.send("wait_for is indeed a cool method")
        
        if msg.content == "y":
            await ctx.send("Perfect! This is your question, you have 120 seconds to answer:")
            question = random.choice(list(CCquestions.keys()))
            await ctx.send(question)

            try: 
                msg = await bot.wait_for('message', check = check, timeout = 120.0)
            except asyncio.TimeoutError:
                await ctx.send(f"**{ctx.author}**, you didn't send any message in the time limit :(")
                return
            else:
                if msg.content == CCquestions[question]:
                    await ctx.send("That's correct! You're so smart!")
                else:
                    await ctx.send("That's not correct, the actual answer was '" + CCquestions[question] + "', but nice try!")

        elif msg.content == "n":
            await ctx.send("Alright! Lets play soon :)")
        else:
            await ctx.send("Sorry, the answer doesn't make sense. . .")
        return

@bot.command()
async def checkflower(ctx):
    if ctx.message.attachments:
        for attachment in ctx.message.attachments:
            file_name = attachment.filename
            file_url= attachment.url
            await attachment.save(f"./images/{file_name}")
            label = get_class(model_path="./keras_model_Flower.h5", labels_path="./labelsFlowers.txt", image_path=f"./images/{file_name}" )
            embed = discord.Embed(title= "This is a... " + label + "!" , description= label +" are such beautiful flowers! Here we'll give you tips to plant them in your garden!", color=0xfc5638)
            if label == "Poppy":
                for f in PoppyTips:
                    embed.add_field(name= "", value= f, inline= False)
            elif label == "Camellia":
                for f in CamelliaTips:
                    embed.add_field(name= "", value= f, inline= False)
            elif label == "Nasturtium":
                for f in NasturtiumTips:
                    embed.add_field(name= "", value= f, inline= False)
            elif label == "Marigold":
                for f in MarigoldTips:
                    embed.add_field(name= "", value= f, inline= False)
            elif label == "Carnation":
                for f in CarnationTips:
                    embed.add_field(name= "", value= f, inline= False)
            elif label == "Chrysantemum":
                for f in ChrysantemumTips:
                    embed.add_field(name= "", value= f, inline= False)
            elif label == "Sunflower":
                for f in SunflowerTips:
                    embed.add_field(name= "", value= f, inline= False)
            elif label == "Hydrangea":
                for f in HydrangeaTips:
                    embed.add_field(name= "", value= f, inline= False)
            elif label == "Jasmine":
                for f in JasmineTips:
                    embed.add_field(name= "", value= f, inline= False)
            elif label == "Lily":
                for f in LilyTips:
                    embed.add_field(name= "", value= f, inline= False)
            elif label == "Daisy":
                for f in DaisyTips:
                    embed.add_field(name= "", value= f, inline= False)
            elif label == "Narcissus":
                for f in NarcissusTips:
                    embed.add_field(name= "", value= f, inline= False)
            elif label == "Orchid":
                for f in OrchidTips:
                    embed.add_field(name= "", value= f, inline= False)
            elif label == "Passionflower":
                for f in PassionflowerTips:
                    embed.add_field(name= "", value= f, inline= False)
            elif label == "Peony":
                for f in PeonyTips:
                    embed.add_field(name= "", value= f, inline= False)
            elif label == "Petunia":
                for f in PetuniaTips:
                    embed.add_field(name= "", value= f, inline= False)
            elif label == "Rose":
                for f in RoseTips:
                    embed.add_field(name= "", value= f, inline= False)
            else:
                for f in TulipTips:
                    embed.add_field(name="", value=f, inline= False)
            await ctx.send(embed=embed)
        
    else:
        await ctx.send("Forgot to upload an image 😞")

@bot.command()
async def checkfruit(ctx):
    if ctx.message.attachments:
        for attachment in ctx.message.attachments:
            file_name = attachment.filename
            file_url= attachment.url
            await attachment.save(f"./images/{file_name}")
            label = get_class(model_path="./keras_model_Fruits.h5", labels_path="./labelsFruits.txt", image_path=f"./images/{file_name}" )
            embed = discord.Embed(title= "This is a... " + label + "!", description= label +" is such a tasty fruit! Here are tips so you can plant this in your garden!", color=0x386dfc)
            
            if label == "Banana":
                for f in BananaTips:
                    embed.add_field(name = "", value=f, inline= False)
            elif label == "Cherry":
                for f in CherryTips:
                    embed.add_field(name = "", value=f, inline= False)
            elif label == "Apricot":
                for f in ApricotTips:
                    embed.add_field(name = "", value=f, inline= False)
            elif label == "Fig":
                for f in FigTips:
                    embed.add_field(name = "", value=f, inline= False)
            elif label == "Kiwi":
                for f in KiwiTips:
                    embed.add_field(name = "", value=f, inline= False)
            elif label == "Lime":
                for f in LimeTips:
                    embed.add_field(name = "", value=f, inline= False)
            elif label == "Lemon":
                for f in LemonTips:
                    embed.add_field(name = "", value=f, inline= False)
            elif label == "Mango":
                for f in MangoTips:
                    embed.add_field(name = "", value=f, inline= False)
            elif label == "Apple":
                for f in AppleTips:
                    embed.add_field(name = "", value=f, inline= False)
            elif label == "Passion Fruit":
                for f in PassionFruitTips:
                    embed.add_field(name = "", value=f, inline= False)
            elif label == "Orange":
                for f in OrangeTips:
                    embed.add_field(name = "", value=f, inline= False)
            elif label == "Avocado":
                for f in AvocadoTips:
                    embed.add_field(name = "", value=f, inline= False)
            elif label == "Pear":
                for f in PearTips:
                    embed.add_field(name="", value=f, inline= False)
            else:
                for f in GrapefruitTips:
                    embed.add_field(name="", value=f, inline= False)
            await ctx.send(embed=embed)
    else:
        await ctx.send("Forgot to upload an image 😞")

@bot.command()
async def checkveggie(ctx):
    if ctx.message.attachments:
        for attachment in ctx.message.attachments:
            file_name = attachment.filename
            file_url= attachment.url
            await attachment.save(f"./images/{file_name}")
            label = get_class(model_path="./keras_model_Veggie.h5", labels_path="./labelsVeggies.txt", image_path=f"./images/{file_name}" )
            embed = discord.Embed(title= "This is a... " + label + "!", description= label + " is such a yummy veggie! Here are some tips to help you grow it!", color=0xfcee38)

            if label == "Eggplant":
                for f in EggplantTips:
                    embed.add_field(name = "", value=f, inline= False)
            elif label == "Brocoli":
                for f in BroccoliTips:
                    embed.add_field(name="", value=f, inline= False)
            elif label == "Onion":
                for f in OnionTips:
                    embed.add_field(name="", value=f, inline= False)
            elif label == "Cauliflower":
                for f in CauliflowerTips:
                    embed.add_field(name="", value=f, inline= False)
            elif label == "Spinach":
                for f in SpinachTips:
                    embed.add_field(name="", value=f, inline= False)
            elif label == "Peas":
                for f in PeasTips:
                    embed.add_field(name="", value=f, inline= False)
            elif label == "Lettuce":
                for f in LettuceTips:
                    embed.add_field(name="", value=f, inline= False)
            elif label == "Chili Pepper":
                for f in ChiliTips:
                    embed.add_field(name="", value=f, inline= False)
            elif label == "Turnip":
                for f in TurnipTips:
                    embed.add_field(name="", value=f, inline= False)
            elif label == "Potato":
                for f in PotatoTips:
                    embed.add_field(name="", value=f, inline= False)
            elif label == "Cucumber":
                for f in CucumberTips:
                    embed.add_field(name="", value=f, inline= False)
            elif label == "Beet":
                for f in BeetTips:
                    embed.add_field(name="", value=f, inline= False)
            elif label == "Cabbage":
                for f in CabbageTips:
                    embed.add_field(name="", value=f,inline= False)
            elif label == "Tomato":
                for f in TomatoTips:
                    embed.add_field(name="", value=f, inline= False)
            elif label == "Carrot":
                for f in CarrotTips:
                    embed.add_field(name="", value=f, inline= False)
            else:
                for f in PumpkinTips:
                    embed.add_field(name="", value=f, inline= False)
            await ctx.send(embed=embed)
    else:
        await ctx.send("Forgot to upload an image 😞")
#--

bot.run("token")