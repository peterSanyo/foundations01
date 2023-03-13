Hand-in 2/5 , Flask Backend
Foundations 2023, CODE University Berlin   
by Péter Sanyó
_______________
Front end stack: 
- HTML 
- CSS
- JavaScript (to come) 

Back end stack:
- Language: Python 
- Server-side web framework and servers: Flask,  Jinja2
__________________
The idea of this website is to grow into an Auction Gallery where 4 objects get to be curated over a time-period of a week. 

Therefore the current structure contains one landing page and 4 product pages which will be further worked on. 
Transitions between each pages should be more fluent in the future. There should be a spacial dimension to the experience of the gallery in the end. 

The product pages are dynamically constructed from a small data library right now. The idea is to make it easy for the operating person to exchange the objects. 
That is why I decided to have 4 product pages with each it's own routes. 
Once the library is expanded, the idea was that by simply changing the name of the product within the function, the whole site will be changed. 
Categories and Keys should stay consistent for different objects, therefore the variables in the HTML-file would also stay consistent. 

object=pieces["old_object"] -> object=pieces["new_object] 

The landing page loops over the items in the library and displays their name and their manufacturer with a link to the productpage itself. 

I would appreciate some input about whether the routes themselves should/can they be further simplified. 
Maybe importing the library in the next steps, when complexity is further added (pictures, videos, media) ? 
Or maybe if this seems good for the specific and consistent functions of each product page. 

Will expand on further functions: 
- Log-in system 
- system to place a bid with an attached letter to the manufacturer. 
- Database 
- Cleaning up the overall structure 
- JS addition 

I appreciate your time reviewing my Hand-In. 
Thanks to the whole foundations-team for their quick responses, their approachability and keeping it engaging while providing relevant ressources along the way. 
