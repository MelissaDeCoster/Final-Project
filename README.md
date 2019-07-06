# Final-Project

Our Final Project attempts to predict crime in the City of Chicago by Community Area and IUCR Code.

<h2>Definitions</h2>
"A community area is one of 77 pre-defined Chicago areas with boundaries that have remained, for the most part, stable since the 1920s. Community areas were created so the census bureau and social scientists could track statistics consistently in defined areas over time" -https://www.tripsavvy.com/chicago-area-neighborhoods-613858

Community Areas are as Follows:

 <Table>
 <tr>
    <th>Code</th>
    <th>Name</th> 
    <th>'Side'</th>
  </tr>
 <tr><td>1</td><td>Rogers Park</td><td>Far North Side</td>
<tr><td>2</td><td>West Ridge</td><td>Far North Side</td>
<tr><td>3</td><td>Uptown</td><td>Far North Side</td>
<tr><td>4</td><td>Lincoln Square</td><td>Far North Side</td>
<tr><td>5</td><td>North Center</td><td>North Side</td>
<tr><td>6</td><td>Lakeview</td><td>North Side</td>
<tr><td>7</td><td>Lincoln Park</td><td>North Side</td>
<tr><td>8</td><td>Near North Side</td><td>Central</td>
<tr><td>9</td><td>Edison Park</td><td>Far North Side</td>
<tr><td>10</td><td>Norwood Park</td><td>Far North Side</td>
<tr><td>11</td><td>Jefferson Park</td><td>Far North Side</td>
<tr><td>12</td><td>Forest Glen</td><td>Far North Side</td>
<tr><td>13</td><td>North Park</td><td>Far North Side</td>
<tr><td>14</td><td>Albany Park</td><td>Far North Side</td>
<tr><td>15</td><td>Portage Park</td><td>Northwest Side</td>
<tr><td>16</td><td>Irving Park</td><td>Northwest Side</td>
<tr><td>17</td><td>Dunning</td><td>Northwest Side</td>
<tr><td>18</td><td>Montclare</td><td>Northwest Side</td>
<tr><td>19</td><td>Belmont Cragin</td><td>Northwest Side</td>
<tr><td>20</td><td>Hermosa</td><td>Northwest Side</td>
<tr><td>21</td><td>Avondale</td><td>North Side</td>
<tr><td>22</td><td>Logan Square</td><td>North Side</td>
<tr><td>23</td><td>Humboldt Park</td><td>West Side</td>
<tr><td>24</td><td>West Town</td><td>West Side</td>
<tr><td>25</td><td>Austin</td><td>West Side</td>
<tr><td>26</td><td>West Garfield Park</td><td>West Side</td>
<tr><td>27</td><td>East Garfield Park</td><td>West Side</td>
<tr><td>28</td><td>Near West Side</td><td>West Side</td>
<tr><td>29</td><td>North Lawndale</td><td>West Side</td>
<tr><td>30</td><td>South Lawndale</td><td>West Side</td>
<tr><td>31</td><td>Lower West Side</td><td>West Side</td>
<tr><td>32</td><td>Loop</td><td>Central</td>
<tr><td>33</td><td>Near South Side</td><td>Central</td>
<tr><td>34</td><td>Armour Square</td><td>South Side</td>
<tr><td>35</td><td>Douglas</td><td>South Side</td>
<tr><td>36</td><td>Oakland</td><td>South Side</td>
<tr><td>37</td><td>Fuller Park</td><td>South Side</td>
<tr><td>38</td><td>Grand Boulevard</td><td>South Side</td>
<tr><td>39</td><td>Kenwood</td><td>South Side</td>
<tr><td>40</td><td>Washington Park</td><td>South Side</td>
<tr><td>41</td><td>Hyde Park</td><td>South Side</td>
<tr><td>42</td><td>Woodlawn</td><td>South Side</td>
<tr><td>43</td><td>South Shore</td><td>South Side</td>
<tr><td>44</td><td>Chatham</td><td>Far Southeast Side</td>
<tr><td>45</td><td>Avalon Park</td><td>Far Southeast Side</td>
<tr><td>46</td><td>South Chicago</td><td>Far Southeast Side</td>
<tr><td>47</td><td>Burnside</td><td>Far Southeast Side</td>
<tr><td>48</td><td>Calumet Heights</td><td>Far Southeast Side</td>
<tr><td>49</td><td>Roseland</td><td>Far Southeast Side</td>
<tr><td>50</td><td>Pullman</td><td>Far Southeast Side</td>
<tr><td>51</td><td>South Deering</td><td>Far Southeast Side</td>
<tr><td>52</td><td>East Side</td><td>Far Southeast Side</td>
<tr><td>53</td><td>West Pullman</td><td>Far Southeast Side</td>
<tr><td>54</td><td>Riverdale</td><td>Far Southeast Side</td>
<tr><td>55</td><td>Hegewisch</td><td>Far Southeast Side</td>
<tr><td>56</td><td>Garfield Ridge</td><td>Southwest Side</td>
<tr><td>57</td><td>Archer Heights</td><td>Southwest Side</td>
<tr><td>58</td><td>Brighton Park</td><td>Southwest Side</td>
<tr><td>59</td><td>McKinley Park</td><td>Southwest Side</td>
<tr><td>60</td><td>Bridgeport</td><td>South Side</td>
<tr><td>61</td><td>New City</td><td>Southwest Side</td>
<tr><td>62</td><td>West Elsdon</td><td>Southwest Side</td>
<tr><td>63</td><td>Gage Park</td><td>Southwest Side</td>
<tr><td>64</td><td>Clearing</td><td>Southwest Side</td>
<tr><td>65</td><td>West Lawn</td><td>Southwest Side</td>
<tr><td>66</td><td>Chicago Lawn</td><td>Southwest Side</td>
<tr><td>67</td><td>West Englewood</td><td>Southwest Side</td>
<tr><td>68</td><td>Englewood</td><td>Southwest Side</td>
<tr><td>69</td><td>Greater Grand Crossing</td><td>South Side</td>
<tr><td>70</td><td>Ashburn</td><td>Far Southwest Side</td>
<tr><td>71</td><td>Auburn Gresham</td><td>Far Southwest Side</td>
<tr><td>72</td><td>Beverly</td><td>Far Southwest Side</td>
<tr><td>73</td><td>Washington Heights</td><td>Far Southwest Side</td>
<tr><td>74</td><td>Mount Greenwood</td><td>Far Southwest Side</td>
<tr><td>75</td><td>Morgan Park</td><td>Far Southwest Side</td>
<tr><td>76</td><td>O'Hare</td><td>Far North Side</td>
<tr><td>77</td><td>Edgewater</td><td>Far North Side</td>
</table>
