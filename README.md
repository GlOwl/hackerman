# Hackerman Quote Generator
The random (fake!) quote generator.  

## Idea

Hollywood and the media in general loves to portrait hackers as these beings that
make computers do anything! They just have to type fast enough,
or at least faster than the hacker on the other side.  

In countless shows and movies, characters say a lot of nonsense
to sound like a real badass hacker.  

If you also want to sound like a badass hacker but struggle to learn the basics
of computer engineering, don't worry, we got you covered!  

We created this sentence generator to make nonsense hacker quotes.  
Grammatically (more or less) correct English sentences mixed with
buzzwords to sound very technical, but don't make any sense.  

**Why?** Because we can! But also because it's fun and these quotes make great
jokes and can be used as placeholder text and descriptions.   

**One more thing...**  just a generator alone would be boring, so we are hosting
a website where anyone can easily get their daily dose of hacker quotes.  
Oh and we are creating an API for anyone to use.  
(Who needs Lorem-Ipsum when you can fill your website with hacker quotes!)  

## Website

Visit [hackerman.wtf](https://hackerman.wtf).  

Demo with placeholder quotes  
<p style="text-align: center">
  <img src="#" width="600" alt="Website demo">
</p>

## API

## Online API

Get a **single** random generated quote at `hackerman.wtf/api`  
Returned is a JSON file
```json
{ "quotes": ["We need to generate the redundant PNG transmitter!"] }
```  
[Try it out](https://hackerman.wtf/api)  

Get **multiple** random generated quotes (max, 100 per query) at `hackerman.wtf/api?n=3`  
Returned is a JSON file
```json
{ "quotes": ["First Quote", "Second Quote", "Third Quote"] }
```  
The parameter `n` sets the number of quotes requested.  
[Try it out](https://hackerman.wtf/api?n=3)  

## Local Generator Script

[...]

## To-Do

**General:**  
- [x] Python sentence generator
- [x] Web API for generating quotes
- [x] Website
- [x] Twitter Bot

**Improvements:**
None, everything is perfect!  

## Credits & Resources

**Authors:**  
- Stefan Kremser [@spacehuhn](https://github.com/spacehuhn)  
- Anatol Pomplun [@GlOwl](https://github.com/GlOwl)

**Tools:**  
- [Python 3](https://www.python.org) Programming Language
- [Django](https://www.djangoproject.com/) Web Framework
- [Bootstrap](https://getbootstrap.com/) Web Library
- [Layoutit](https://www.layoutit.com/) Bootstrap Builder
- [Lumen](https://bootswatch.com/lumen/) Bootstrap Theme
- [jQuery](https://jquery.com/) JavaScript Framework

## License

This software is licensed under the MIT License. See the [license file](LICENSE) for details.  
