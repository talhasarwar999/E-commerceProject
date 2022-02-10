I have sorted out three methods for maping clean.csv into mogodb
1- use it as a single record without differentiating between reading and station

reading :{
        id:'1',
        .
        . 
        .
        prefrence: 'resourc etc.'            
}

2- use reading and station as one entity but station within reading 

reading :{
        id:'1',
        .
        . 
        .
        station :{
            id: 22
            location: 'xyz'
            geopoints: '2323,4564'
        }
        .
        .
        prefrence: 'resourc etc.'            
}   

3- use reading and station as complete seprate collection 
station :{
            id: 22
            location: 'xyz'
            geopoints: '2323,4564'
}    
reading :{
        id:'1',
        station_id : 22,
        .
        .
        .
        prefrence: 'resourc etc.'            
}   
    
Each method has it's own plus minus first and thirdmethod is more logical,understandable and readable so we will 
continue with 3rd method.

Implementation details:
1. Load file into mongodb by following command  mongoimport --type csv -d dmf -c readings --headerline --drop clean.csv 
2. Run command  mongo  to start mongo terminal.
3. Run command use dmf;. (DMF is our database that we have created through our terminal)
4. Run command db.readings.all();. which will return all record available in our file.(as we can't show all the records so this is output of following db.readings.find().pretty().limit(5) command.)
Output(Shell):

json
{
    "_id" : ObjectId("61d599ea118d4651b6a06717"),
    "Date Time" : "2013-08-23T07:00:00+00:00",
    "NOx" : "51p54044",
    "NO2" : "30p50055",
    "NO" : "13p72186",
    "SiteID" : 452,
    "PM10" : "27p8",
    "NVPM10" : "23p2",
    "VPM10" : "4p6",
    "NVPM2.5" : "16p4",
    "PM2.5" : "19p454",
    "VPM2.5" : "2p9",
    "CO" : "",
    "O3" : "20p40603",
    "SO2" : "",
    "Temperature" : "",
    "RH" : "",
    "Air Pressure" : "",
    "Location" : "AURN St Pauls",
    "geo_point_2d" : "51p4628294172,-2p58454081635",
    "DateStart" : "2006-06-15T00:00:00+00:00",
    "DateEnd" : "",
    "Current" : "",
    "Instrument Type" : "True",
    "field23" : "Continuous (Reference)"
}
{
    "_id" : ObjectId("61d599ea118d4651b6a06718"),
    "Date Time" : "2013-08-23T08:00:00+00:00",
    "NOx" : "94p5",
    "NO2" : "44p25",
    "NO" : "33p0",
    "SiteID" : 203,
    "PM10" : "",
    "NVPM10" : "",
    "VPM10" : "",
    "NVPM2.5" : "",
    "PM2.5" : "",
    "VPM2.5" : "",
    "CO" : "",
    "O3" : "",
    "SO2" : "",
    "Temperature" : "",
    "RH" : "",
    "Air Pressure" : "",
    "Location" : "Brislington Depot",
    "geo_point_2d" : "51p4417471802,-2p55995583224",
    "DateStart" : "2001-01-01T00:00:00+00:00",
    "DateEnd" : "",
    "Current" : "",
    "Instrument Type" : "True",
    "field23" : "Continuous (Reference)"
}
{
    "_id" : ObjectId("61d599ea118d4651b6a06719"),
    "Date Time" : "2013-08-23T10:00:00+00:00",
    "NOx" : "242p75",
    "NO2" : "59p75",
    "NO" : "119p5",
    "SiteID" : 206,
    "PM10" : "",
    "NVPM10" : "",
    "VPM10" : "",
    "NVPM2.5" : "",
    "PM2.5" : "",
    "VPM2.5" : "",
    "CO" : "",
    "O3" : "",
    "SO2" : "",
    "Temperature" : "",
    "RH" : "",
    "Air Pressure" : "",
    "Location" : "Rupert Street",
    "geo_point_2d" : "51p4554331987,-2p59626237324",
    "DateStart" : "2003-01-01T00:00:00+00:00",
    "DateEnd" : "2015-12-31T00:00:00+00:00",
    "Current" : "",
    "Instrument Type" : "False",
    "field23" : "Continuous (Reference)"
}
{
    "_id" : ObjectId("61d599ea118d4651b6a0671a"),
    "Date Time" : "2013-08-23T14:00:00+00:00",
    "NOx" : "197p75",
    "NO2" : "73p25",
    "NO" : "81p25",
    "SiteID" : 270,
    "PM10" : "",
    "NVPM10" : "",
    "VPM10" : "",
    "NVPM2.5" : "",
    "PM2.5" : "",
    "VPM2.5" : "",
    "CO" : "",
    "O3" : "",
    "SO2" : "",
    "Temperature" : "",
    "RH" : "",
    "Air Pressure" : "",
    "Location" : "Wells Road",
    "geo_point_2d" : "51p4278638883,-2p56374153315",
    "DateStart" : "2003-05-23T00:00:00+00:00",
    "DateEnd" : "",
    "Current" : "",
    "Instrument Type" : "True",
    "field23" : "Continuous (Reference)"
}
{
    "_id" : ObjectId("61d599ea118d4651b6a0671b"),
    "Date Time" : "2013-08-23T18:00:00+00:00",
    "NOx" : "81p0",
    "NO2" : "55p5",
    "NO" : "16p5",
    "SiteID" : 203,
    "PM10" : "",
    "NVPM10" : "",
    "VPM10" : "",
    "NVPM2.5" : "",
    "PM2.5" : "",
    "VPM2.5" : "",
    "CO" : "",
    "O3" : "",
    "SO2" : "",
    "Temperature" : "",
    "RH" : "",
    "Air Pressure" : "",
    "Location" : "Brislington Depot",
    "geo_point_2d" : "51p4417471802,-2p55995583224",
    "DateStart" : "2001-01-01T00:00:00+00:00",
    "DateEnd" : "",
    "Current" : "",
    "Instrument Type" : "True",
    "field23" : "Continuous (Reference)"
} 




Here our first method impletemented we run queries on this readings collection.
### SQL-a query:-
SELECT reading.datetime,station.location,reading.nox FROM reading,station WHERE reading.nox = (SELECT MAX(nox) FROM reading WHERE YEAR(reading.datetime) = 2019) AND reading.stationid = station.stationid AND YEAR(reading.datetime) =2019;
### MONGOdb query:-
As we are handling reading and station as one record so query will be simplified; (we are using JavaScript Syntax for query because it is allowed in MongoDB)
var firstNOx = 0;
db.readings.find().forEach(
    function(reading){
        if(new Date(reading['Date Time']).getFullYear() == 2019)
        {    
        if (reading['NOx'] >firstNOx) 
            {
                firstNOx = reading['NOx']
            }
        }
    })
db.readings.find().forEach(
    function(reading){
        if(reading['NOx'] == firstNOx )
        {    
            print(reading['Date Time'],reading['Location'],reading['NOx'])
        }
    })

output:-

2019-01-24T09:00:00+00:00 Colston Avenue 1403.5