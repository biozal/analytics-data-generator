# Couchbase Analytics Data Generator
This repo contains the item.gen.py script that is used to generate items that will be stored in the beer_item.json file.  The data format and rules are loosely based on CH3 which you can find more information about here (see page 65): https://www.tpc.org/tpc_documents_current_versions/pdf/tpc-c_v5.11.0.pdf

### Usage:
```python
python3 item_gen.py 
```

## Warehouses

The data found in the warehouse.json file was scrapped from Wikipedia's list of states and cities based on population:
https://en.wikipedia.org/wiki/List_of_largest_cities_of_U.S._states_and_territories_by_population

## Districts
Districts were mostly populated using two APIs:
https://www.zipcodeapi.com/API

Zip Code API was used with a distance of 20 miles to generate the 10 districts per warehouse.  To generate the geo locations, Google's API was used for this:  
https://developers.google.com/maps/documentation/geocoding/start

<br><br>
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
