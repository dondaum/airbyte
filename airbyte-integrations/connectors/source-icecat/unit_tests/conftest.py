import json

from pytest import fixture


@fixture
def config():
    return {
        "catalog_type": "Open Icecat",
        "catalog_language": "EN",
        "identifier_type": {"type": "productid", "value": "1198270"},
        "username": "openIcecat-live",
        "password": "pwd",
    }


@fixture
def gtinconfig():
    return {
        "catalog_type": "Open Icecat",
        "catalog_language": "EN",
        "identifier_type": {"type": "GTIN", "value": "0882780751682"},
        "username": "openIcecat-live",
        "password": "pwd",
    }


@fixture
def badconfig():
    return {
        "catalog_type": "Open Icecat",
        "catalog_language": "EN",
        "identifier_type": {"type": "productcode", "value": "12345D"},
        "username": "openIcecat-live",
        "password": "pwd",
    }


@fixture(name="icecat_response")
def valid_response():
    raw_json = """{"msg":"OK","data":{"Dictionary":{"zoom_panel_dragg":"Mouse dragging","specs":"Specs","link_integrate_desk":"How to integrate Icecat LIVE JavaScript.","release_date":"Release date","model_name":"Product name","reviews_head_name":"Reviews","prod_code":"Product code","eu_energy_label":"EU Energy Label","eu_product_fiche":"EU Product Fiche","marketing_text":"","options_head_name":"Options","ean_code":"EAN/UPC code","reasons_to_buy":"Reasons to buy","demo_msg_part3":"If you don't have an Icecat account, please register here for free.","video":"Video","demo_msg_part1":"You are using now a Demo account. Please, use your own Icecat account","product_family":"Product family","html_content":"","zoom_panel_out":"Zoom out","zoom_panel_in":"Zoom in","product_series":"Product series","demo_insert_desc":"This is a demo of a seamless insert of an Icecat LIVE product data-sheet in your website. Imagine that this responsive data-sheet is included in the product page of your webshop.","supplier_name":"Brand","pdf_url":"User manual","flash360":"3D tour","cat_name":"Category","zoom_panel_init":"Original size","pdf_specs":"Product Brochure","back_to_top":"Back to top","desc":"Description","demo_msg_part2":"your Icecat login name"},"GeneralInfo":{"IcecatId":1198270,"ReleaseDate":"10-08-2007","EndOfLifeDate":"","Title":"HP Compaq 6710b Base Model Notebook PC","TitleInfo":{"GeneratedIntTitle":"HP Compaq 6710b Base Model Notebook PC","GeneratedLocalTitle":{"Value":"HP Compaq 6710b Base Model Notebook PC","Language":"EN"},"BrandLocalTitle":{"Value":"","Language":"EN"}},"Brand":"HP","BrandID":"1","BrandLogo":"https://images.icecat.biz/img/brand/thumb/1_cf8603f6de7b4c4d8ac4f5f0ef439a05.jpg","BrandInfo":{"BrandName":"HP","BrandLocalName":"","BrandLogo":"https://images.icecat.biz/img/brand/thumb/1_cf8603f6de7b4c4d8ac4f5f0ef439a05.jpg"},"ProductName":"Compaq 6710b Base Model Notebook PC","ProductNameInfo":{"ProductIntName":"Compaq 6710b Base Model Notebook PC","ProductLocalName":{"Value":"","Language":"EN"}},"BrandPartCode":"RJ459AV","GTIN":["0882780751682","882780751682"],"Category":{"CategoryID":"151","Name":{"Value":"Notebooks","Language":"EN"}},"ProductFamily":{},"ProductSeries":{"SeriesID":"1"},"Description":{"ID":"21805998","LongDesc":"","LongProductName":"","MiddleDesc":"","Disclaimer":"","ManualPDFURL":"","ManualPDFSize":"0","LeafletPDFURL":"","PDFSize":"0","URL":"","WarrantyInfo":"HP Services offers limited 3-year and 1-year standard parts and laborpick-up or carry-in, and toll-free 7 x 24 hardware technical phone support (depending on model); 1-year limitedon primary battery. On-site service andupgrades are also available.","Updated":"2015-02-25 14:36:53","Language":"US"},"SummaryDescription":{"ShortSummaryDescription":"HP Compaq 6710b Base Model Notebook PC","LongSummaryDescription":"HP Compaq 6710b Base Model Notebook PC"},"BulletPoints":{},"GeneratedBulletPoints":{}},"Image":{"HighPic":"https://images.icecat.biz/img/norm/high/1198270-HP.jpg","HighPicSize":"47168","HighPicHeight":"400","HighPicWidth":"400","LowPic":"https://images.icecat.biz/img/norm/low/1198270-HP.jpg","LowPicSize":"19156","LowPicHeight":"200","LowPicWidth":"200","Pic500x500":"https://images.icecat.biz/img/gallery_mediums/img_1198270_medium_1480991259_2453_5647.jpg","Pic500x500Size":"119360","Pic500x500Height":"500","Pic500x500Width":"500","ThumbPic":"https://images.icecat.biz/thumbs/1198270.jpg","ThumbPicSize":"4595"},"Multimedia":[{"ID":"6F93BCEA-E7E7-11E3-B083-99D01F7ADADF","URL":"https://objects.icecat.biz/objects/HP_literature_emea_en_c00990687.pdf","Type":"other digital assets","ContentType":"application/pdf","KeepAsUrl":"0","Description":"quickspecs","Size":"281408","IsPrivate":"0","Updated":"2022-07-11 13:41:19","Language":"EN","IsVideo":0}],"Gallery":[{"ID":"13532323","LowPic":"https://images.icecat.biz/img/norm/low/1198270-HP.jpg","LowSize":"19156","LowHeight":"200","LowWidth":"200","ThumbPic":"https://images.icecat.biz/thumbs/1198270.jpg","ThumbPicSize":"4595","Pic":"https://images.icecat.biz/img/norm/high/1198270-HP.jpg","Size":"47168","PicHeight":"400","PicWidth":"400","Pic500x500":"https://images.icecat.biz/img/gallery_mediums/img_1198270_medium_1480991259_2453_5647.jpg","Pic500x500Size":"119360","Pic500x500Height":"500","Pic500x500Width":"500","No":"1","IsMain":"Y","Updated":"2019-04-04 08:07:23","IsPrivate":"0","Type":"ProductImage","Attributes":{"OriginalFileName":""}}],"FeaturesGroups":[],"FeatureLogos":[],"ReasonsToBuy":[],"Reviews":[{"AwardHighPic":"","AwardLogoPic":"","BottomLine":"","Code":"","DateAdded":"","Group":"","ID":10827,"LogoPic":"","Score":70,"URL":"","Updated":"","Value":"HPs Compaq range targets the corporate user and small businesses, offering robust build quality and a conservative but practical design. The HP Compaq 6710b (£699 inc. VAT) features a 15.4-inch display. It uses standard TFT technology – so the display...","ValueBad":"No 802.11n, Pricey","ValueGood":"Tough build, Powerful performance, Good battery life","Language":"EN","IcecatID":1198270}],"TaxonomyDescriptions":[],"ProductRelated":[{"ID":187772895,"CategoryID":195,"Preferred":0,"IcecatID":92924034,"ProductCode":"H3T50AA#AC3","ThumbPic":"","ProductName":"X4000b Bluetooth Mouse","Brand":"HP","BrandID":1,"ProductRelatedLocales":[{"ID":0,"Language":"EN","Preferred":0,"StartDate":"","EndDate":""}]},{"ID":154638039,"CategoryID":977,"Preferred":0,"IcecatID":33447789,"ProductCode":"NSVGALOCK","ThumbPic":"","ProductName":"Neomounts by Newstar security lock cable","Brand":"Neomounts by Newstar","BrandID":290,"ProductRelatedLocales":[{"ID":0,"Language":"EN","Preferred":0,"StartDate":"","EndDate":""}]},{"ID":128556785,"CategoryID":2034,"Preferred":0,"IcecatID":14702705,"ProductCode":"NS-CS200BLACK","ThumbPic":"","ProductName":"Neomounts by Newstar cable sock","Brand":"Neomounts by Newstar","BrandID":290,"ProductRelatedLocales":[{"ID":0,"Language":"EN","Preferred":0,"StartDate":"","EndDate":""}]},{"ID":113110239,"CategoryID":194,"Preferred":0,"IcecatID":5799340,"ProductCode":"RC465AA","ThumbPic":"","ProductName":"USB Keyboard and Mouse Bundle","Brand":"HP","BrandID":1,"ProductRelatedLocales":[{"ID":0,"Language":"EN","Preferred":0,"StartDate":"","EndDate":""}]},{"ID":128230557,"CategoryID":1514,"Preferred":0,"IcecatID":4152840,"ProductCode":"NSLS100","ThumbPic":"","ProductName":"Neomounts by Newstar foldable laptop stand","Brand":"Neomounts by Newstar","BrandID":290,"ProductRelatedLocales":[{"ID":0,"Language":"EN","Preferred":0,"StartDate":"","EndDate":""}]},{"ID":127954160,"CategoryID":1514,"Preferred":0,"IcecatID":1351682,"ProductCode":"NOTEBOOK-D100","ThumbPic":"","ProductName":"Neomounts by Newstar laptop desk mount","Brand":"Neomounts by Newstar","BrandID":290,"ProductRelatedLocales":[{"ID":0,"Language":"EN","Preferred":0,"StartDate":"","EndDate":""}]},{"ID":113110241,"CategoryID":911,"Preferred":0,"IcecatID":558345,"ProductCode":"KTH-ZD8000B/2G","ThumbPic":"","ProductName":"2GB DDR2-667","Brand":"Kingston Technology","BrandID":18,"ProductRelatedLocales":[{"ID":0,"Language":"EN","Preferred":0,"StartDate":"","EndDate":""}]},{"ID":113110240,"CategoryID":911,"Preferred":0,"IcecatID":459203,"ProductCode":"KTH-ZD8000B/1G","ThumbPic":"","ProductName":"1GB DDR2-667","Brand":"Kingston Technology","BrandID":18,"ProductRelatedLocales":[{"ID":0,"Language":"EN","Preferred":0,"StartDate":"","EndDate":""}]}],"Variants":[],"ProductStory":[],"DemoAccount":true}}"""
    return json.loads(raw_json)


@fixture
def product_raw_resp():
    return """[{
      "msg": "OK",
      "data": {
        "Dictionary": {
          "zoom_panel_dragg": "Mouse dragging",
          "specs": "Specs",
          "link_integrate_desk": "How to integrate Icecat LIVE JavaScript.",
          "release_date": "Release date",
          "model_name": "Product name",
          "reviews_head_name": "Reviews",
          "prod_code": "Product code",
          "eu_energy_label": "EU Energy Label",
          "eu_product_fiche": "EU Product Fiche",
          "marketing_text": "",
          "options_head_name": "Options",
          "ean_code": "EAN/UPC code",
          "reasons_to_buy": "Reasons to buy",
          "demo_msg_part3": "If you don't have an Icecat account, please register here for free.",
          "video": "Video",
          "demo_msg_part1": "You are using now a Demo account. Please, use your own Icecat account",
          "product_family": "Product family",
          "html_content": "",
          "zoom_panel_out": "Zoom out",
          "zoom_panel_in": "Zoom in",
          "product_series": "Product series",
          "demo_insert_desc": "This is a demo of a seamless insert of an Icecat LIVE product data-sheet in your website. Imagine that this responsive data-sheet is included in the product page of your webshop.",
          "supplier_name": "Brand",
          "pdf_url": "User manual",
          "flash360": "3D tour",
          "cat_name": "Category",
          "zoom_panel_init": "Original size",
          "pdf_specs": "Product Brochure",
          "back_to_top": "Back to top",
          "desc": "Description",
          "demo_msg_part2": "your Icecat login name"
        },
        "GeneralInfo": {
          "IcecatId": 1438185,
          "ReleaseDate": "15-06-2008",
          "EndOfLifeDate": "30-09-2008",
          "Title": "HP Compaq 6710b Notebook PC",
          "TitleInfo": {
            "GeneratedIntTitle": "HP KE125ET notebook",
            "GeneratedLocalTitle": {
              "Value": "HP KE125ET notebook",
              "Language": "EN"
            },
            "BrandLocalTitle": {
              "Value": "HP Compaq 6710b Notebook PC",
              "Language": "EN"
            }
          },
          "Brand": "HP",
          "BrandID": "1",
          "BrandLogo": "https://images.icecat.biz/img/brand/thumb/1_cf8603f6de7b4c4d8ac4f5f0ef439a05.jpg",
          "BrandInfo": {
            "BrandName": "HP",
            "BrandLocalName": "",
            "BrandLogo": "https://images.icecat.biz/img/brand/thumb/1_cf8603f6de7b4c4d8ac4f5f0ef439a05.jpg"
          },
          "ProductName": "Compaq 6710b Notebook PC",
          "ProductNameInfo": {
            "ProductIntName": "KE125ET",
            "ProductLocalName": {
              "Value": "Compaq 6710b Notebook PC",
              "Language": "EN"
            }
          },
          "BrandPartCode": "KE125ET",
          "GTIN": [
            "0884420156116",
            "884420156116",
            "0883585922451",
            "883585922451",
            "0884420151241",
            "884420151241",
            "0883585931712",
            "883585931712",
            "0883585927579",
            "883585927579",
            "0883585927562",
            "883585927562",
            "0883585922710",
            "883585922710"
          ],
          "Category": {
            "CategoryID": "151",
            "Name": {
              "Value": "Notebooks",
              "Language": "EN"
            }
          },
          "ProductFamily": {},
          "ProductSeries": {
            "SeriesID": "1"
          },
          "Description": {
            "ID": "21908052",
            "LongDesc": "",
            "LongProductName": " Compaq 6710b Notebook PC",
            "MiddleDesc": "",
            "Disclaimer": "",
            "ManualPDFURL": "",
            "ManualPDFSize": "0",
            "LeafletPDFURL": "",
            "PDFSize": "0",
            "URL": "https://www8.hp.com",
            "WarrantyInfo": "",
            "Updated": "2020-03-13 12:23:55",
            "Language": "EN"
          },
          "SummaryDescription": {
            "ShortSummaryDescription": "HP Compaq 6710b Notebook PC",
            "LongSummaryDescription": "HP Compaq 6710b Notebook PC"
          },
          "BulletPoints": {},
          "GeneratedBulletPoints": {}
        },
        "Image": {
          "HighPic": "https://images.icecat.biz/img/gallery/1438185_1788599811.jpg",
          "HighPicSize": "1567100",
          "HighPicHeight": "2385",
          "HighPicWidth": "2647",
          "LowPic": "https://images.icecat.biz/img/gallery_lows/1438185_1788599811.jpg",
          "LowPicSize": "20476",
          "LowPicHeight": "180",
          "LowPicWidth": "200",
          "Pic500x500": "https://images.icecat.biz/img/gallery_mediums/1438185_1788599811.jpg",
          "Pic500x500Size": "118638",
          "Pic500x500Height": "450",
          "Pic500x500Width": "500",
          "ThumbPic": "https://images.icecat.biz/img/gallery_thumbs/1438185_1788599811.jpg",
          "ThumbPicSize": "4814"
        },
        "Multimedia": [
          {
            "ID": "44EF4385-38D2-4231-A952-4F03A266E50B",
            "URL": "https://link.brightcove.com/services/player/bcpidrklftdZcfg?bckey=",
            "Type": "video/mp4",
            "ContentType": "text/html",
            "KeepAsUrl": "1",
            "Description": "HP ENVY Notebooks",
            "Size": "587",
            "IsPrivate": "0",
            "Updated": "2018-02-17 05:34:23",
            "Language": "EN",
            "IsVideo": 1,
            "ThumbUrl": "",
            "PreviewUrl": ""
          },
          {
            "ID": "4B52FB38-E7E8-11E3-B0ED-BD3E0BC1EBBA",
            "URL": "https://objects.icecat.biz/objects/HP_literature_emea_en_c00990687.pdf",
            "Type": "other digital assets",
            "ContentType": "application/pdf",
            "KeepAsUrl": "0",
            "Description": "quickspecs",
            "Size": "281408",
            "IsPrivate": "0",
            "Updated": "2022-07-11 13:41:20",
            "Language": "EN",
            "IsVideo": 0
          }
        ],
        "Gallery": [
          {
            "ID": "24502701",
            "LowPic": "https://images.icecat.biz/img/gallery_lows/1438185_1788599811.jpg",
            "LowSize": "20476",
            "LowHeight": "180",
            "LowWidth": "200",
            "ThumbPic": "https://images.icecat.biz/img/gallery_thumbs/1438185_1788599811.jpg",
            "ThumbPicSize": "4814",
            "Pic": "https://images.icecat.biz/img/gallery/1438185_1788599811.jpg",
            "Size": "1567100",
            "PicHeight": "2385",
            "PicWidth": "2647",
            "Pic500x500": "https://images.icecat.biz/img/gallery_mediums/1438185_1788599811.jpg",
            "Pic500x500Size": "118638",
            "Pic500x500Height": "450",
            "Pic500x500Width": "500",
            "No": "1",
            "IsMain": "Y",
            "Updated": "2018-11-23 01:27:34",
            "IsPrivate": "0",
            "Type": "ProductImage",
            "Attributes": {
              "OriginalFileName": ""
            }
          }
        ],
        "FeaturesGroups": [],
        "FeatureLogos": [],
        "ReasonsToBuy": [],
        "Reviews": [
          {
            "AwardHighPic": "",
            "AwardLogoPic": "",
            "BottomLine": "",
            "Code": "",
            "DateAdded": "",
            "Group": "",
            "ID": 10827,
            "LogoPic": "",
            "Score": 70,
            "URL": "",
            "Updated": "",
            "Value": "HPs Compaq range targets the corporate user and small businesses, offering robust build quality and a conservative but practical design. The HP Compaq 6710b (£699 inc. VAT) features a 15.4-inch display. It uses standard TFT technology – so the display...",
            "ValueBad": "No 802.11n, Pricey",
            "ValueGood": "Tough build, Powerful performance, Good battery life",
            "Language": "EN",
            "IcecatID": 1438185
          }
        ],
        "TaxonomyDescriptions": [],
        "ProductRelated": [
          {
            "ID": 48885380,
            "CategoryID": 788,
            "Preferred": 0,
            "IcecatID": 61858,
            "ProductCode": "U4386E",
            "ThumbPic": "",
            "ProductName": "U4386E",
            "Brand": "HP",
            "BrandID": 1,
            "ProductRelatedLocales": [
              {
                "ID": 0,
                "Language": "EN",
                "Preferred": 0,
                "StartDate": "",
                "EndDate": ""
              }
            ]
          },
          {
            "ID": 25126102,
            "CategoryID": 788,
            "Preferred": 0,
            "IcecatID": 61856,
            "ProductCode": "U4388PE",
            "ThumbPic": "",
            "ProductName": "1Y Post Warranty NBD Onsite Notebook Service",
            "Brand": "HP",
            "BrandID": 1,
            "ProductRelatedLocales": [
              {
                "ID": 0,
                "Language": "EN",
                "Preferred": 0,
                "StartDate": "",
                "EndDate": ""
              }
            ]
          },
          {
            "ID": 25126118,
            "CategoryID": 788,
            "Preferred": 0,
            "IcecatID": 1352915,
            "ProductCode": "UF240E",
            "ThumbPic": "",
            "ProductName": "3 year Next Business Day Onsite w/Accidental Damage Protection Commercial Notebook Service",
            "Brand": "HP",
            "BrandID": 1,
            "ProductRelatedLocales": [
              {
                "ID": 0,
                "Language": "EN",
                "Preferred": 0,
                "StartDate": "",
                "EndDate": ""
              }
            ]
          },
          {
            "ID": 25126106,
            "CategoryID": 788,
            "Preferred": 0,
            "IcecatID": 135645,
            "ProductCode": "U7874E",
            "ThumbPic": "",
            "ProductName": "4Y",
            "Brand": "HP",
            "BrandID": 1,
            "ProductRelatedLocales": [
              {
                "ID": 0,
                "Language": "EN",
                "Preferred": 0,
                "StartDate": "",
                "EndDate": ""
              }
            ]
          },
          {
            "ID": 66744461,
            "CategoryID": 788,
            "Preferred": 0,
            "IcecatID": 3597690,
            "ProductCode": "UQ816PE",
            "ThumbPic": "",
            "ProductName": "1 year Post Warranty Travel NextBusDay Onsite w/Accidental Damage Protection Gen 2/DMR NB OnlySVC",
            "Brand": "HP",
            "BrandID": 1,
            "ProductRelatedLocales": [
              {
                "ID": 0,
                "Language": "EN",
                "Preferred": 0,
                "StartDate": "",
                "EndDate": ""
              }
            ]
          },
          {
            "ID": 66738443,
            "CategoryID": 788,
            "Preferred": 0,
            "IcecatID": 3597629,
            "ProductCode": "UQ815PE",
            "ThumbPic": "",
            "ProductName": "UQ815PE",
            "Brand": "HP",
            "BrandID": 1,
            "ProductRelatedLocales": [
              {
                "ID": 0,
                "Language": "EN",
                "Preferred": 0,
                "StartDate": "",
                "EndDate": ""
              }
            ]
          },
          {
            "ID": 27783379,
            "CategoryID": 788,
            "Preferred": 0,
            "IcecatID": 1794865,
            "ProductCode": "U4395A#*PM",
            "ThumbPic": "",
            "ProductName": "3 year Pickup and Return Commercial Notebook Only Service",
            "Brand": "HP",
            "BrandID": 1,
            "ProductRelatedLocales": [
              {
                "ID": 0,
                "Language": "EN",
                "Preferred": 0,
                "StartDate": "",
                "EndDate": ""
              }
            ]
          },
          {
            "ID": 26875561,
            "CategoryID": 788,
            "Preferred": 0,
            "IcecatID": 95939,
            "ProductCode": "U4395A",
            "ThumbPic": "",
            "ProductName": "3 year Pickup and Return Notebook Hardware Support",
            "Brand": "HP",
            "BrandID": 1,
            "ProductRelatedLocales": [
              {
                "ID": 0,
                "Language": "EN",
                "Preferred": 0,
                "StartDate": "",
                "EndDate": ""
              }
            ]
          },
          {
            "ID": 26851578,
            "CategoryID": 788,
            "Preferred": 0,
            "IcecatID": 41935,
            "ProductCode": "U4386A",
            "ThumbPic": "",
            "ProductName": "U4386A",
            "Brand": "HP",
            "BrandID": 1,
            "ProductRelatedLocales": [
              {
                "ID": 0,
                "Language": "EN",
                "Preferred": 0,
                "StartDate": "",
                "EndDate": ""
              }
            ]
          },
          {
            "ID": 25745245,
            "CategoryID": 222,
            "Preferred": 0,
            "IcecatID": 1633369,
            "ProductCode": "GX008AA#ABB?EON",
            "ThumbPic": "",
            "ProductName": "L2245w 22-inch Widescreen LCD Monitor",
            "Brand": "HP",
            "BrandID": 1,
            "ProductRelatedLocales": [
              {
                "ID": 0,
                "Language": "EN",
                "Preferred": 0,
                "StartDate": "",
                "EndDate": ""
              }
            ]
          },
          {
            "ID": 25745244,
            "CategoryID": 222,
            "Preferred": 0,
            "IcecatID": 1581951,
            "ProductCode": "GX008AA#BB",
            "ThumbPic": "",
            "ProductName": "L2245w 22-inch Widescreen LCD Monitor",
            "Brand": "HP",
            "BrandID": 1,
            "ProductRelatedLocales": [
              {
                "ID": 0,
                "Language": "EN",
                "Preferred": 0,
                "StartDate": "",
                "EndDate": ""
              }
            ]
          },
          {
            "ID": 25745242,
            "CategoryID": 222,
            "Preferred": 0,
            "IcecatID": 1401651,
            "ProductCode": "GX008AA",
            "ThumbPic": "",
            "ProductName": "L2245w 22-inch Widescreen LCD Monitor",
            "Brand": "HP",
            "BrandID": 1,
            "ProductRelatedLocales": [
              {
                "ID": 0,
                "Language": "EN",
                "Preferred": 0,
                "StartDate": "",
                "EndDate": ""
              }
            ]
          },
          {
            "ID": 70348961,
            "CategoryID": 1285,
            "Preferred": 0,
            "IcecatID": 877095,
            "ProductCode": "GD405AA",
            "ThumbPic": "",
            "ProductName": "Deluxe Roller Case",
            "Brand": "HP",
            "BrandID": 1,
            "ProductRelatedLocales": [
              {
                "ID": 0,
                "Language": "EN",
                "Preferred": 0,
                "StartDate": "",
                "EndDate": ""
              }
            ]
          },
          {
            "ID": 50470187,
            "CategoryID": 1285,
            "Preferred": 0,
            "IcecatID": 797828,
            "ProductCode": "RR316AA",
            "ThumbPic": "",
            "ProductName": "Executive Leather Case",
            "Brand": "HP",
            "BrandID": 1,
            "ProductRelatedLocales": [
              {
                "ID": 0,
                "Language": "EN",
                "Preferred": 0,
                "StartDate": "",
                "EndDate": ""
              }
            ]
          },
          {
            "ID": 21918438,
            "CategoryID": 222,
            "Preferred": 0,
            "IcecatID": 647994,
            "ProductCode": "RB145AA",
            "ThumbPic": "",
            "ProductName": "L2045w",
            "Brand": "HP",
            "BrandID": 1,
            "ProductRelatedLocales": [
              {
                "ID": 0,
                "Language": "EN",
                "Preferred": 0,
                "StartDate": "",
                "EndDate": ""
              }
            ]
          },
          {
            "ID": 48885625,
            "CategoryID": 195,
            "Preferred": 0,
            "IcecatID": 558184,
            "ProductCode": "RJ316AA",
            "ThumbPic": "",
            "ProductName": "RJ316AA",
            "Brand": "HP",
            "BrandID": 1,
            "ProductRelatedLocales": [
              {
                "ID": 0,
                "Language": "EN",
                "Preferred": 0,
                "StartDate": "",
                "EndDate": ""
              }
            ]
          },
          {
            "ID": 48885455,
            "CategoryID": 2509,
            "Preferred": 0,
            "IcecatID": 456197,
            "ProductCode": "EJ092AA",
            "ThumbPic": "",
            "ProductName": "12-cell Ultra-capacity Battery with Adapter",
            "Brand": "HP",
            "BrandID": 1,
            "ProductRelatedLocales": [
              {
                "ID": 0,
                "Language": "EN",
                "Preferred": 0,
                "StartDate": "",
                "EndDate": ""
              }
            ]
          },
          {
            "ID": 50470083,
            "CategoryID": 152,
            "Preferred": 0,
            "IcecatID": 444992,
            "ProductCode": "EN489AA",
            "ThumbPic": "",
            "ProductName": "EN489AA",
            "Brand": "HP",
            "BrandID": 1,
            "ProductRelatedLocales": [
              {
                "ID": 0,
                "Language": "EN",
                "Preferred": 0,
                "StartDate": "",
                "EndDate": ""
              }
            ]
          },
          {
            "ID": 48885400,
            "CategoryID": 1514,
            "Preferred": 0,
            "IcecatID": 265194,
            "ProductCode": "PA508A",
            "ThumbPic": "",
            "ProductName": "Adjustable Stand",
            "Brand": "HP",
            "BrandID": 1,
            "ProductRelatedLocales": [
              {
                "ID": 0,
                "Language": "EN",
                "Preferred": 0,
                "StartDate": "",
                "EndDate": ""
              }
            ]
          },
          {
            "ID": 25126108,
            "CategoryID": 788,
            "Preferred": 0,
            "IcecatID": 443773,
            "ProductCode": "U7876E",
            "ThumbPic": "",
            "ProductName": "5y Nbd Notebook 1ywty CPU HW Support",
            "Brand": "Hewlett Packard Enterprise",
            "BrandID": 13357,
            "ProductRelatedLocales": [
              {
                "ID": 0,
                "Language": "EN",
                "Preferred": 0,
                "StartDate": "",
                "EndDate": ""
              }
            ]
          },
          {
            "ID": 160862344,
            "CategoryID": 12,
            "Preferred": 0,
            "IcecatID": 35712320,
            "ProductCode": "X7W31AA",
            "ThumbPic": "",
            "ProductName": "Microsoft Office 2016 Home and Business Software",
            "Brand": "HP",
            "BrandID": 1,
            "ProductRelatedLocales": [
              {
                "ID": 0,
                "Language": "EN",
                "Preferred": 0,
                "StartDate": "",
                "EndDate": ""
              }
            ]
          },
          {
            "ID": 164077608,
            "CategoryID": 1637,
            "Preferred": 0,
            "IcecatID": 35712312,
            "ProductCode": "X1H26AA",
            "ThumbPic": "",
            "ProductName": "Plantronics Blackwire C310-M",
            "Brand": "HP",
            "BrandID": 1,
            "ProductRelatedLocales": [
              {
                "ID": 0,
                "Language": "EN",
                "Preferred": 0,
                "StartDate": "",
                "EndDate": ""
              }
            ]
          },
          {
            "ID": 164077519,
            "CategoryID": 1637,
            "Preferred": 0,
            "IcecatID": 35712311,
            "ProductCode": "X1H25AA",
            "ThumbPic": "",
            "ProductName": "Plantronics Voyager Focus UC B825-M",
            "Brand": "HP",
            "BrandID": 1,
            "ProductRelatedLocales": [
              {
                "ID": 0,
                "Language": "EN",
                "Preferred": 0,
                "StartDate": "",
                "EndDate": ""
              }
            ]
          },
          {
            "ID": 163978354,
            "CategoryID": 1637,
            "Preferred": 0,
            "IcecatID": 35712310,
            "ProductCode": "X1H24AA",
            "ThumbPic": "",
            "ProductName": "Plantronics Voyager Legend UC B235-M",
            "Brand": "HP",
            "BrandID": 1,
            "ProductRelatedLocales": [
              {
                "ID": 0,
                "Language": "EN",
                "Preferred": 0,
                "StartDate": "",
                "EndDate": ""
              }
            ]
          },
          {
            "ID": 163978338,
            "CategoryID": 1637,
            "Preferred": 0,
            "IcecatID": 33526633,
            "ProductCode": "X1H27AA",
            "ThumbPic": "",
            "ProductName": "Plantronics Blackwire 325.1-M",
            "Brand": "HP",
            "BrandID": 1,
            "ProductRelatedLocales": [
              {
                "ID": 0,
                "Language": "EN",
                "Preferred": 0,
                "StartDate": "",
                "EndDate": ""
              }
            ]
          },
          {
            "ID": 154643924,
            "CategoryID": 977,
            "Preferred": 0,
            "IcecatID": 33447789,
            "ProductCode": "NSVGALOCK",
            "ThumbPic": "",
            "ProductName": "Neomounts by Newstar security lock cable",
            "Brand": "Neomounts by Newstar",
            "BrandID": 290,
            "ProductRelatedLocales": [
              {
                "ID": 0,
                "Language": "EN",
                "Preferred": 0,
                "StartDate": "",
                "EndDate": ""
              }
            ]
          },
          {
            "ID": 148436802,
            "CategoryID": 152,
            "Preferred": 0,
            "IcecatID": 23331723,
            "ProductCode": "FQ834AA - NEW OPEN BOX",
            "ThumbPic": "",
            "ProductName": "USB 2.0 Docking Station",
            "Brand": "HP",
            "BrandID": 1,
            "ProductRelatedLocales": [
              {
                "ID": 0,
                "Language": "EN",
                "Preferred": 0,
                "StartDate": "",
                "EndDate": ""
              }
            ]
          },
          {
            "ID": 165272995,
            "CategoryID": 195,
            "Preferred": 0,
            "IcecatID": 19587027,
            "ProductCode": "H6F25AA",
            "ThumbPic": "",
            "ProductName": "Ultra Mobile Wireless Mouse",
            "Brand": "HP",
            "BrandID": 1,
            "ProductRelatedLocales": [
              {
                "ID": 0,
                "Language": "EN",
                "Preferred": 0,
                "StartDate": "",
                "EndDate": ""
              }
            ]
          },
          {
            "ID": 134514474,
            "CategoryID": 194,
            "Preferred": 0,
            "IcecatID": 18501874,
            "ProductCode": "DT527A",
            "ThumbPic": "",
            "ProductName": "PS/2 Standard Keyboard",
            "Brand": "HP",
            "BrandID": 1,
            "ProductRelatedLocales": [
              {
                "ID": 0,
                "Language": "EN",
                "Preferred": 0,
                "StartDate": "",
                "EndDate": ""
              }
            ]
          },
          {
            "ID": 150777484,
            "CategoryID": 152,
            "Preferred": 0,
            "IcecatID": 18331305,
            "ProductCode": "KP080ET#ABB-RFB",
            "ThumbPic": "",
            "ProductName": "2008 120W Docking Station",
            "Brand": "HP",
            "BrandID": 1,
            "ProductRelatedLocales": [
              {
                "ID": 0,
                "Language": "EN",
                "Preferred": 0,
                "StartDate": "",
                "EndDate": ""
              }
            ]
          },
          {
            "ID": 114422572,
            "CategoryID": 827,
            "Preferred": 0,
            "IcecatID": 16669864,
            "ProductCode": "ED495ET#ABB",
            "ThumbPic": "",
            "ProductName": "90W Smart AC Adapter",
            "Brand": "HP",
            "BrandID": 1,
            "ProductRelatedLocales": [
              {
                "ID": 0,
                "Language": "EN",
                "Preferred": 0,
                "StartDate": "",
                "EndDate": ""
              }
            ]
          },
          {
            "ID": 114514196,
            "CategoryID": 827,
            "Preferred": 0,
            "IcecatID": 16668689,
            "ProductCode": "ED495AA#ABB",
            "ThumbPic": "",
            "ProductName": "90W Smart AC Adapter",
            "Brand": "HP",
            "BrandID": 1,
            "ProductRelatedLocales": [
              {
                "ID": 0,
                "Language": "EN",
                "Preferred": 0,
                "StartDate": "",
                "EndDate": ""
              }
            ]
          },
          {
            "ID": 134501192,
            "CategoryID": 194,
            "Preferred": 0,
            "IcecatID": 16668618,
            "ProductCode": "DT527A#ABB",
            "ThumbPic": "",
            "ProductName": "PS/2 Standard Keyboard",
            "Brand": "HP",
            "BrandID": 1,
            "ProductRelatedLocales": [
              {
                "ID": 0,
                "Language": "EN",
                "Preferred": 0,
                "StartDate": "",
                "EndDate": ""
              }
            ]
          },
          {
            "ID": 114580748,
            "CategoryID": 827,
            "Preferred": 0,
            "IcecatID": 16668502,
            "ProductCode": "AJ652AA#ABB",
            "ThumbPic": "",
            "ProductName": "90W Smart AC/Auto/Air Combo Adapter",
            "Brand": "HP",
            "BrandID": 1,
            "ProductRelatedLocales": [
              {
                "ID": 0,
                "Language": "EN",
                "Preferred": 0,
                "StartDate": "",
                "EndDate": ""
              }
            ]
          },
          {
            "ID": 134489589,
            "CategoryID": 194,
            "Preferred": 0,
            "IcecatID": 16668021,
            "ProductCode": "DT528A#ABB",
            "ThumbPic": "",
            "ProductName": "USB Standard Keyboard",
            "Brand": "HP",
            "BrandID": 1,
            "ProductRelatedLocales": [
              {
                "ID": 0,
                "Language": "EN",
                "Preferred": 0,
                "StartDate": "",
                "EndDate": ""
              }
            ]
          },
          {
            "ID": 114639895,
            "CategoryID": 869,
            "Preferred": 0,
            "IcecatID": 16667732,
            "ProductCode": "DC851B#ABB",
            "ThumbPic": "",
            "ProductName": "DC851B",
            "Brand": "HP",
            "BrandID": 1,
            "ProductRelatedLocales": [
              {
                "ID": 0,
                "Language": "EN",
                "Preferred": 0,
                "StartDate": "",
                "EndDate": ""
              }
            ]
          },
          {
            "ID": 114662604,
            "CategoryID": 869,
            "Preferred": 0,
            "IcecatID": 16565411,
            "ProductCode": "DC851B#B13",
            "ThumbPic": "",
            "ProductName": "DC851B",
            "Brand": "HP",
            "BrandID": 1,
            "ProductRelatedLocales": [
              {
                "ID": 0,
                "Language": "EN",
                "Preferred": 0,
                "StartDate": "",
                "EndDate": ""
              }
            ]
          },
          {
            "ID": 134482959,
            "CategoryID": 194,
            "Preferred": 0,
            "IcecatID": 16485367,
            "ProductCode": "DT528A#B13",
            "ThumbPic": "",
            "ProductName": "USB Standard Keyboard",
            "Brand": "HP",
            "BrandID": 1,
            "ProductRelatedLocales": [
              {
                "ID": 0,
                "Language": "EN",
                "Preferred": 0,
                "StartDate": "",
                "EndDate": ""
              }
            ]
          },
          {
            "ID": 134480875,
            "CategoryID": 194,
            "Preferred": 0,
            "IcecatID": 16485366,
            "ProductCode": "DT527A#B13",
            "ThumbPic": "",
            "ProductName": "PS/2 Standard Keyboard",
            "Brand": "HP",
            "BrandID": 1,
            "ProductRelatedLocales": [
              {
                "ID": 0,
                "Language": "EN",
                "Preferred": 0,
                "StartDate": "",
                "EndDate": ""
              }
            ]
          },
          {
            "ID": 114426933,
            "CategoryID": 827,
            "Preferred": 0,
            "IcecatID": 16485255,
            "ProductCode": "ED495ET#B13",
            "ThumbPic": "",
            "ProductName": "ED495ET",
            "Brand": "HP",
            "BrandID": 1,
            "ProductRelatedLocales": [
              {
                "ID": 0,
                "Language": "EN",
                "Preferred": 0,
                "StartDate": "",
                "EndDate": ""
              }
            ]
          },
          {
            "ID": 114537664,
            "CategoryID": 827,
            "Preferred": 0,
            "IcecatID": 16483721,
            "ProductCode": "ED495AA#B13",
            "ThumbPic": "",
            "ProductName": "90W Smart AC Adapter",
            "Brand": "HP",
            "BrandID": 1,
            "ProductRelatedLocales": [
              {
                "ID": 0,
                "Language": "EN",
                "Preferred": 0,
                "StartDate": "",
                "EndDate": ""
              }
            ]
          },
          {
            "ID": 114597804,
            "CategoryID": 827,
            "Preferred": 0,
            "IcecatID": 16483717,
            "ProductCode": "AJ652AA#B13",
            "ThumbPic": "",
            "ProductName": "90W Smart AC/Auto/Air Combo Adapter",
            "Brand": "HP",
            "BrandID": 1,
            "ProductRelatedLocales": [
              {
                "ID": 0,
                "Language": "EN",
                "Preferred": 0,
                "StartDate": "",
                "EndDate": ""
              }
            ]
          },
          {
            "ID": 113985830,
            "CategoryID": 152,
            "Preferred": 0,
            "IcecatID": 16213354,
            "ProductCode": "FQ834AA",
            "ThumbPic": "",
            "ProductName": "FQ834AA",
            "Brand": "HP",
            "BrandID": 1,
            "ProductRelatedLocales": [
              {
                "ID": 0,
                "Language": "EN",
                "Preferred": 0,
                "StartDate": "",
                "EndDate": ""
              }
            ]
          },
          {
            "ID": 165272987,
            "CategoryID": 195,
            "Preferred": 0,
            "IcecatID": 15928663,
            "ProductCode": "H3T50AA",
            "ThumbPic": "",
            "ProductName": "X4000b Bluetooth Mouse",
            "Brand": "HP",
            "BrandID": 1,
            "ProductRelatedLocales": [
              {
                "ID": 0,
                "Language": "EN",
                "Preferred": 0,
                "StartDate": "",
                "EndDate": ""
              }
            ]
          },
          {
            "ID": 128563306,
            "CategoryID": 2034,
            "Preferred": 0,
            "IcecatID": 14702705,
            "ProductCode": "NS-CS200BLACK",
            "ThumbPic": "",
            "ProductName": "Neomounts by Newstar cable sock",
            "Brand": "Neomounts by Newstar",
            "BrandID": 290,
            "ProductRelatedLocales": [
              {
                "ID": 0,
                "Language": "EN",
                "Preferred": 0,
                "StartDate": "",
                "EndDate": ""
              }
            ]
          },
          {
            "ID": 165272989,
            "CategoryID": 1285,
            "Preferred": 0,
            "IcecatID": 14457566,
            "ProductCode": "H2W17AA",
            "ThumbPic": "",
            "ProductName": "Essential Top Load",
            "Brand": "HP",
            "BrandID": 1,
            "ProductRelatedLocales": [
              {
                "ID": 0,
                "Language": "EN",
                "Preferred": 0,
                "StartDate": "",
                "EndDate": ""
              }
            ]
          },
          {
            "ID": 165272996,
            "CategoryID": 1285,
            "Preferred": 0,
            "IcecatID": 14291054,
            "ProductCode": "H1D25AA",
            "ThumbPic": "",
            "ProductName": "Essential Messenger Case",
            "Brand": "HP",
            "BrandID": 1,
            "ProductRelatedLocales": [
              {
                "ID": 0,
                "Language": "EN",
                "Preferred": 0,
                "StartDate": "",
                "EndDate": ""
              }
            ]
          },
          {
            "ID": 95939789,
            "CategoryID": 195,
            "Preferred": 0,
            "IcecatID": 11815262,
            "ProductCode": "DC369A",
            "ThumbPic": "",
            "ProductName": "DC369A",
            "Brand": "HP",
            "BrandID": 1,
            "ProductRelatedLocales": [
              {
                "ID": 0,
                "Language": "EN",
                "Preferred": 0,
                "StartDate": "",
                "EndDate": ""
              }
            ]
          },
          {
            "ID": 134461773,
            "CategoryID": 194,
            "Preferred": 0,
            "IcecatID": 9498262,
            "ProductCode": "DT528A#GRK",
            "ThumbPic": "",
            "ProductName": "USB Standard",
            "Brand": "HP",
            "BrandID": 1,
            "ProductRelatedLocales": [
              {
                "ID": 0,
                "Language": "EN",
                "Preferred": 0,
                "StartDate": "",
                "EndDate": ""
              }
            ]
          },
          {
            "ID": 88821391,
            "CategoryID": 152,
            "Preferred": 0,
            "IcecatID": 8012889,
            "ProductCode": "KP080AA#ABH",
            "ThumbPic": "",
            "ProductName": "KP080AA",
            "Brand": "HP",
            "BrandID": 1,
            "ProductRelatedLocales": [
              {
                "ID": 0,
                "Language": "EN",
                "Preferred": 0,
                "StartDate": "",
                "EndDate": ""
              }
            ]
          },
          {
            "ID": 165272993,
            "CategoryID": 942,
            "Preferred": 0,
            "IcecatID": 7803395,
            "ProductCode": "AW664AA",
            "ThumbPic": "",
            "ProductName": "Adjustable Dual Display Stand",
            "Brand": "HP",
            "BrandID": 1,
            "ProductRelatedLocales": [
              {
                "ID": 0,
                "Language": "EN",
                "Preferred": 0,
                "StartDate": "",
                "EndDate": ""
              }
            ]
          },
          {
            "ID": 79775243,
            "CategoryID": 803,
            "Preferred": 0,
            "IcecatID": 5844992,
            "ProductCode": "RZ364A#ABH",
            "ThumbPic": "",
            "ProductName": "Microsoft Office Professional 2007 Activation License - HP Media-less License",
            "Brand": "HP",
            "BrandID": 1,
            "ProductRelatedLocales": [
              {
                "ID": 0,
                "Language": "EN",
                "Preferred": 0,
                "StartDate": "",
                "EndDate": ""
              }
            ]
          },
          {
            "ID": 88703837,
            "CategoryID": 911,
            "Preferred": 0,
            "IcecatID": 4745330,
            "ProductCode": "EM993AA",
            "ThumbPic": "",
            "ProductName": "512-MB (DDR2 667 MHz) SODIMM",
            "Brand": "HP",
            "BrandID": 1,
            "ProductRelatedLocales": [
              {
                "ID": 0,
                "Language": "EN",
                "Preferred": 0,
                "StartDate": "",
                "EndDate": ""
              }
            ]
          },
          {
            "ID": 128235591,
            "CategoryID": 1514,
            "Preferred": 0,
            "IcecatID": 4152840,
            "ProductCode": "NSLS100",
            "ThumbPic": "",
            "ProductName": "Neomounts by Newstar foldable laptop stand",
            "Brand": "Neomounts by Newstar",
            "BrandID": 290,
            "ProductRelatedLocales": [
              {
                "ID": 0,
                "Language": "EN",
                "Preferred": 0,
                "StartDate": "",
                "EndDate": ""
              }
            ]
          },
          {
            "ID": 114589348,
            "CategoryID": 827,
            "Preferred": 0,
            "IcecatID": 3445320,
            "ProductCode": "AJ652AA#ABH",
            "ThumbPic": "",
            "ProductName": "90W Smart AC/Auto/Air Combo Adapter",
            "Brand": "HP",
            "BrandID": 1,
            "ProductRelatedLocales": [
              {
                "ID": 0,
                "Language": "EN",
                "Preferred": 0,
                "StartDate": "",
                "EndDate": ""
              }
            ]
          },
          {
            "ID": 48886065,
            "CategoryID": 152,
            "Preferred": 0,
            "IcecatID": 3331784,
            "ProductCode": "AK155AA",
            "ThumbPic": "",
            "ProductName": "AK155AA",
            "Brand": "HP",
            "BrandID": 1,
            "ProductRelatedLocales": [
              {
                "ID": 0,
                "Language": "EN",
                "Preferred": 0,
                "StartDate": "",
                "EndDate": ""
              }
            ]
          },
          {
            "ID": 64065329,
            "CategoryID": 577,
            "Preferred": 0,
            "IcecatID": 2399355,
            "ProductCode": "GX607AA",
            "ThumbPic": "",
            "ProductName": "Elite Autofocus Webcam",
            "Brand": "HP",
            "BrandID": 1,
            "ProductRelatedLocales": [
              {
                "ID": 0,
                "Language": "EN",
                "Preferred": 0,
                "StartDate": "",
                "EndDate": ""
              }
            ]
          },
          {
            "ID": 64103799,
            "CategoryID": 577,
            "Preferred": 0,
            "IcecatID": 2389941,
            "ProductCode": "KQ245AA",
            "ThumbPic": "",
            "ProductName": "Premium Autofocus Webcam",
            "Brand": "HP",
            "BrandID": 1,
            "ProductRelatedLocales": [
              {
                "ID": 0,
                "Language": "EN",
                "Preferred": 0,
                "StartDate": "",
                "EndDate": ""
              }
            ]
          },
          {
            "ID": 114608601,
            "CategoryID": 827,
            "Preferred": 0,
            "IcecatID": 2131141,
            "ProductCode": "AJ652AA",
            "ThumbPic": "",
            "ProductName": "90W Smart AC/Auto/Air Combo Adapter",
            "Brand": "HP",
            "BrandID": 1,
            "ProductRelatedLocales": [
              {
                "ID": 0,
                "Language": "EN",
                "Preferred": 0,
                "StartDate": "",
                "EndDate": ""
              }
            ]
          },
          {
            "ID": 64079157,
            "CategoryID": 1637,
            "Preferred": 0,
            "IcecatID": 2090019,
            "ProductCode": "KJ270AA",
            "ThumbPic": "",
            "ProductName": "Digital Premium Stereo Headset",
            "Brand": "HP",
            "BrandID": 1,
            "ProductRelatedLocales": [
              {
                "ID": 0,
                "Language": "EN",
                "Preferred": 0,
                "StartDate": "",
                "EndDate": ""
              }
            ]
          },
          {
            "ID": 74753933,
            "CategoryID": 152,
            "Preferred": 0,
            "IcecatID": 1973718,
            "ProductCode": "FQ834ET",
            "ThumbPic": "",
            "ProductName": "USB 2.0 Docking Station",
            "Brand": "HP",
            "BrandID": 1,
            "ProductRelatedLocales": [
              {
                "ID": 0,
                "Language": "EN",
                "Preferred": 0,
                "StartDate": "",
                "EndDate": ""
              }
            ]
          },
          {
            "ID": 74744186,
            "CategoryID": 152,
            "Preferred": 0,
            "IcecatID": 1947167,
            "ProductCode": "FQ834ET#AC3",
            "ThumbPic": "",
            "ProductName": "USB 2.0 Docking Station",
            "Brand": "HP",
            "BrandID": 1,
            "ProductRelatedLocales": [
              {
                "ID": 0,
                "Language": "EN",
                "Preferred": 0,
                "StartDate": "",
                "EndDate": ""
              }
            ]
          },
          {
            "ID": 28798440,
            "CategoryID": 803,
            "Preferred": 0,
            "IcecatID": 1946301,
            "ProductCode": "GE318T#ABD?PREIS",
            "ThumbPic": "",
            "ProductName": "Microsoft® Office Small Business 2007",
            "Brand": "HP",
            "BrandID": 1,
            "ProductRelatedLocales": [
              {
                "ID": 0,
                "Language": "EN",
                "Preferred": 0,
                "StartDate": "",
                "EndDate": ""
              }
            ]
          },
          {
            "ID": 28548552,
            "CategoryID": 1285,
            "Preferred": 0,
            "IcecatID": 1933137,
            "ProductCode": "RR315AA#",
            "ThumbPic": "",
            "ProductName": "Universal Nylon Case",
            "Brand": "HP",
            "BrandID": 1,
            "ProductRelatedLocales": [
              {
                "ID": 0,
                "Language": "EN",
                "Preferred": 0,
                "StartDate": "",
                "EndDate": ""
              }
            ]
          },
          {
            "ID": 28798441,
            "CategoryID": 803,
            "Preferred": 0,
            "IcecatID": 1908549,
            "ProductCode": "GE316T#ABD?PREIS",
            "ThumbPic": "",
            "ProductName": "Microsoft® Office Basic Edition 2007",
            "Brand": "HP",
            "BrandID": 1,
            "ProductRelatedLocales": [
              {
                "ID": 0,
                "Language": "EN",
                "Preferred": 0,
                "StartDate": "",
                "EndDate": ""
              }
            ]
          },
          {
            "ID": 28798446,
            "CategoryID": 152,
            "Preferred": 0,
            "IcecatID": 1906211,
            "ProductCode": "KP080ET#STAND",
            "ThumbPic": "",
            "ProductName": "2008 120W Docking Station",
            "Brand": "HP",
            "BrandID": 1,
            "ProductRelatedLocales": [
              {
                "ID": 0,
                "Language": "EN",
                "Preferred": 0,
                "StartDate": "",
                "EndDate": ""
              }
            ]
          },
          {
            "ID": 79613626,
            "CategoryID": 2315,
            "Preferred": 0,
            "IcecatID": 1905213,
            "ProductCode": "FS944AA",
            "ThumbPic": "",
            "ProductName": "Mobile Audio Speakers",
            "Brand": "HP",
            "BrandID": 1,
            "ProductRelatedLocales": [
              {
                "ID": 0,
                "Language": "EN",
                "Preferred": 0,
                "StartDate": "",
                "EndDate": ""
              }
            ]
          },
          {
            "ID": 28798442,
            "CategoryID": 803,
            "Preferred": 0,
            "IcecatID": 1897463,
            "ProductCode": "GE317T#ABD?PREIS",
            "ThumbPic": "",
            "ProductName": "Microsoft® Office Professional Edition 2007",
            "Brand": "HP",
            "BrandID": 1,
            "ProductRelatedLocales": [
              {
                "ID": 0,
                "Language": "EN",
                "Preferred": 0,
                "StartDate": "",
                "EndDate": ""
              }
            ]
          },
          {
            "ID": 79611330,
            "CategoryID": 1514,
            "Preferred": 0,
            "IcecatID": 1895138,
            "ProductCode": "AL549AA",
            "ThumbPic": "",
            "ProductName": "AL549AA",
            "Brand": "HP",
            "BrandID": 1,
            "ProductRelatedLocales": [
              {
                "ID": 0,
                "Language": "EN",
                "Preferred": 0,
                "StartDate": "",
                "EndDate": ""
              }
            ]
          },
          {
            "ID": 79610353,
            "CategoryID": 152,
            "Preferred": 0,
            "IcecatID": 1893954,
            "ProductCode": "FQ834AA#AC3",
            "ThumbPic": "",
            "ProductName": "USB 2.0 Docking Station",
            "Brand": "HP",
            "BrandID": 1,
            "ProductRelatedLocales": [
              {
                "ID": 0,
                "Language": "EN",
                "Preferred": 0,
                "StartDate": "",
                "EndDate": ""
              }
            ]
          },
          {
            "ID": 28798438,
            "CategoryID": 814,
            "Preferred": 0,
            "IcecatID": 1893861,
            "ProductCode": "EJ092AA#B13/KIT4",
            "ThumbPic": "",
            "ProductName": "Ultra-Capacity Battery",
            "Brand": "HP",
            "BrandID": 1,
            "ProductRelatedLocales": [
              {
                "ID": 0,
                "Language": "EN",
                "Preferred": 0,
                "StartDate": "",
                "EndDate": ""
              }
            ]
          },
          {
            "ID": 28178708,
            "CategoryID": 814,
            "Preferred": 0,
            "IcecatID": 1853208,
            "ProductCode": "EJ092AA#B13/KIT3",
            "ThumbPic": "",
            "ProductName": "Ultra-Capacity Battery",
            "Brand": "HP",
            "BrandID": 1,
            "ProductRelatedLocales": [
              {
                "ID": 0,
                "Language": "EN",
                "Preferred": 0,
                "StartDate": "",
                "EndDate": ""
              }
            ]
          },
          {
            "ID": 62969824,
            "CategoryID": 1285,
            "Preferred": 0,
            "IcecatID": 1806290,
            "ProductCode": "AP355ET",
            "ThumbPic": "",
            "ProductName": "AP355ET",
            "Brand": "HP",
            "BrandID": 1,
            "ProductRelatedLocales": [
              {
                "ID": 0,
                "Language": "EN",
                "Preferred": 0,
                "StartDate": "",
                "EndDate": ""
              }
            ]
          },
          {
            "ID": 27727942,
            "CategoryID": 152,
            "Preferred": 0,
            "IcecatID": 1774303,
            "ProductCode": "KP080AA#UUZ#*KIT",
            "ThumbPic": "",
            "ProductName": "2008 120W Docking Station",
            "Brand": "HP",
            "BrandID": 1,
            "ProductRelatedLocales": [
              {
                "ID": 0,
                "Language": "EN",
                "Preferred": 0,
                "StartDate": "",
                "EndDate": ""
              }
            ]
          },
          {
            "ID": 27727943,
            "CategoryID": 152,
            "Preferred": 0,
            "IcecatID": 1774302,
            "ProductCode": "KP081AA#UUZ#*KIT",
            "ThumbPic": "",
            "ProductName": "2008 150W Advanced Docking Station",
            "Brand": "HP",
            "BrandID": 1,
            "ProductRelatedLocales": [
              {
                "ID": 0,
                "Language": "EN",
                "Preferred": 0,
                "StartDate": "",
                "EndDate": ""
              }
            ]
          },
          {
            "ID": 79601916,
            "CategoryID": 1285,
            "Preferred": 0,
            "IcecatID": 1748705,
            "ProductCode": "AP355AA",
            "ThumbPic": "",
            "ProductName": "Basic Messenger ",
            "Brand": "HP",
            "BrandID": 1,
            "ProductRelatedLocales": [
              {
                "ID": 0,
                "Language": "EN",
                "Preferred": 0,
                "StartDate": "",
                "EndDate": ""
              }
            ]
          },
          {
            "ID": 27289169,
            "CategoryID": 1285,
            "Preferred": 0,
            "IcecatID": 1747857,
            "ProductCode": "PR277AA#*LADY PACK",
            "ThumbPic": "",
            "ProductName": "Women's Signature Leather Notebook Bag - Black",
            "Brand": "HP",
            "BrandID": 1,
            "ProductRelatedLocales": [
              {
                "ID": 0,
                "Language": "EN",
                "Preferred": 0,
                "StartDate": "",
                "EndDate": ""
              }
            ]
          },
          {
            "ID": 27289174,
            "CategoryID": 152,
            "Preferred": 0,
            "IcecatID": 1747798,
            "ProductCode": "KQ751AA#PERFECT WS",
            "ThumbPic": "",
            "ProductName": "2008 150W Docking Station",
            "Brand": "HP",
            "BrandID": 1,
            "ProductRelatedLocales": [
              {
                "ID": 0,
                "Language": "EN",
                "Preferred": 0,
                "StartDate": "",
                "EndDate": ""
              }
            ]
          },
          {
            "ID": 27289173,
            "CategoryID": 152,
            "Preferred": 0,
            "IcecatID": 1747796,
            "ProductCode": "KQ751AA#*PERFECT WS",
            "ThumbPic": "",
            "ProductName": "2008 150W Docking Station",
            "Brand": "HP",
            "BrandID": 1,
            "ProductRelatedLocales": [
              {
                "ID": 0,
                "Language": "EN",
                "Preferred": 0,
                "StartDate": "",
                "EndDate": ""
              }
            ]
          },
          {
            "ID": 27289175,
            "CategoryID": 152,
            "Preferred": 0,
            "IcecatID": 1747765,
            "ProductCode": "KP080ET#PERFECT NEW",
            "ThumbPic": "",
            "ProductName": "2008 120W Docking Station",
            "Brand": "HP",
            "BrandID": 1,
            "ProductRelatedLocales": [
              {
                "ID": 0,
                "Language": "EN",
                "Preferred": 0,
                "StartDate": "",
                "EndDate": ""
              }
            ]
          },
          {
            "ID": 27289170,
            "CategoryID": 1285,
            "Preferred": 0,
            "IcecatID": 1747763,
            "ProductCode": "PT186AA#*LADY PACK",
            "ThumbPic": "",
            "ProductName": "Women's Signature Leather Notebook Bag - Red",
            "Brand": "HP",
            "BrandID": 1,
            "ProductRelatedLocales": [
              {
                "ID": 0,
                "Language": "EN",
                "Preferred": 0,
                "StartDate": "",
                "EndDate": ""
              }
            ]
          },
          {
            "ID": 26639967,
            "CategoryID": 152,
            "Preferred": 0,
            "IcecatID": 1739103,
            "ProductCode": "KP080ET#ABB/KIT",
            "ThumbPic": "",
            "ProductName": "2008 120W Docking Station",
            "Brand": "HP",
            "BrandID": 1,
            "ProductRelatedLocales": [
              {
                "ID": 0,
                "Language": "EN",
                "Preferred": 0,
                "StartDate": "",
                "EndDate": ""
              }
            ]
          },
          {
            "ID": 26639966,
            "CategoryID": 152,
            "Preferred": 0,
            "IcecatID": 1739102,
            "ProductCode": "KP080ET#ABB/KIT1",
            "ThumbPic": "",
            "ProductName": "2008 120W Docking Station",
            "Brand": "HP",
            "BrandID": 1,
            "ProductRelatedLocales": [
              {
                "ID": 0,
                "Language": "EN",
                "Preferred": 0,
                "StartDate": "",
                "EndDate": ""
              }
            ]
          },
          {
            "ID": 26639965,
            "CategoryID": 152,
            "Preferred": 0,
            "IcecatID": 1739100,
            "ProductCode": "KQ751AA#ABB/KIT",
            "ThumbPic": "",
            "ProductName": "2008 150W Docking Station",
            "Brand": "HP",
            "BrandID": 1,
            "ProductRelatedLocales": [
              {
                "ID": 0,
                "Language": "EN",
                "Preferred": 0,
                "StartDate": "",
                "EndDate": ""
              }
            ]
          },
          {
            "ID": 26639964,
            "CategoryID": 152,
            "Preferred": 0,
            "IcecatID": 1739095,
            "ProductCode": "KQ751AA#ABB/KIT1",
            "ThumbPic": "",
            "ProductName": "2008 150W Docking Station",
            "Brand": "HP",
            "BrandID": 1,
            "ProductRelatedLocales": [
              {
                "ID": 0,
                "Language": "EN",
                "Preferred": 0,
                "StartDate": "",
                "EndDate": ""
              }
            ]
          },
          {
            "ID": 62038499,
            "CategoryID": 152,
            "Preferred": 0,
            "IcecatID": 1726663,
            "ProductCode": "KP081ET",
            "ThumbPic": "",
            "ProductName": "2008 150W Advanced Docking Station",
            "Brand": "HP",
            "BrandID": 1,
            "ProductRelatedLocales": [
              {
                "ID": 0,
                "Language": "EN",
                "Preferred": 0,
                "StartDate": "",
                "EndDate": ""
              }
            ]
          },
          {
            "ID": 26639947,
            "CategoryID": 194,
            "Preferred": 0,
            "IcecatID": 1724642,
            "ProductCode": "GM322AA",
            "ThumbPic": "",
            "ProductName": "GM322AA",
            "Brand": "HP",
            "BrandID": 1,
            "ProductRelatedLocales": [
              {
                "ID": 0,
                "Language": "EN",
                "Preferred": 0,
                "StartDate": "",
                "EndDate": ""
              }
            ]
          },
          {
            "ID": 62031011,
            "CategoryID": 1285,
            "Preferred": 0,
            "IcecatID": 1723728,
            "ProductCode": "AM863ET",
            "ThumbPic": "",
            "ProductName": "AM863ET",
            "Brand": "HP",
            "BrandID": 1,
            "ProductRelatedLocales": [
              {
                "ID": 0,
                "Language": "EN",
                "Preferred": 0,
                "StartDate": "",
                "EndDate": ""
              }
            ]
          },
          {
            "ID": 26490324,
            "CategoryID": 152,
            "Preferred": 0,
            "IcecatID": 1717424,
            "ProductCode": "EN488AA#ABB/KIT2",
            "ThumbPic": "",
            "ProductName": "Basic Docking Station with Smart AC Adapter",
            "Brand": "HP",
            "BrandID": 1,
            "ProductRelatedLocales": [
              {
                "ID": 0,
                "Language": "EN",
                "Preferred": 0,
                "StartDate": "",
                "EndDate": ""
              }
            ]
          },
          {
            "ID": 78530607,
            "CategoryID": 858,
            "Preferred": 0,
            "IcecatID": 1714108,
            "ProductCode": "FE477ET",
            "ThumbPic": "",
            "ProductName": "250GB Pocket Media Drive",
            "Brand": "HP",
            "BrandID": 1,
            "ProductRelatedLocales": [
              {
                "ID": 0,
                "Language": "EN",
                "Preferred": 0,
                "StartDate": "",
                "EndDate": ""
              }
            ]
          },
          {
            "ID": 77636752,
            "CategoryID": 577,
            "Preferred": 0,
            "IcecatID": 1712707,
            "ProductCode": "KQ246AA",
            "ThumbPic": "",
            "ProductName": "Deluxe Webcam",
            "Brand": "HP",
            "BrandID": 1,
            "ProductRelatedLocales": [
              {
                "ID": 0,
                "Language": "EN",
                "Preferred": 0,
                "StartDate": "",
                "EndDate": ""
              }
            ]
          },
          {
            "ID": 26442738,
            "CategoryID": 152,
            "Preferred": 0,
            "IcecatID": 1700131,
            "ProductCode": "EN488AA#ABB/KIT1",
            "ThumbPic": "",
            "ProductName": "Basic Docking Station with Smart AC Adapter",
            "Brand": "HP",
            "BrandID": 1,
            "ProductRelatedLocales": [
              {
                "ID": 0,
                "Language": "EN",
                "Preferred": 0,
                "StartDate": "",
                "EndDate": ""
              }
            ]
          },
          {
            "ID": 79585519,
            "CategoryID": 911,
            "Preferred": 0,
            "IcecatID": 1685442,
            "ProductCode": "KT294ET",
            "ThumbPic": "",
            "ProductName": "PC2-6400 4GB",
            "Brand": "HP",
            "BrandID": 1,
            "ProductRelatedLocales": [
              {
                "ID": 0,
                "Language": "EN",
                "Preferred": 0,
                "StartDate": "",
                "EndDate": ""
              }
            ]
          },
          {
            "ID": 79585025,
            "CategoryID": 911,
            "Preferred": 0,
            "IcecatID": 1685436,
            "ProductCode": "KT293ET",
            "ThumbPic": "",
            "ProductName": "2-GB 800 MHz PC2-6400 DDR2 SODIMM",
            "Brand": "HP",
            "BrandID": 1,
            "ProductRelatedLocales": [
              {
                "ID": 0,
                "Language": "EN",
                "Preferred": 0,
                "StartDate": "",
                "EndDate": ""
              }
            ]
          },
          {
            "ID": 25520509,
            "CategoryID": 152,
            "Preferred": 0,
            "IcecatID": 1648202,
            "ProductCode": "KP080ET",
            "ThumbPic": "",
            "ProductName": "2008 120W Docking Station",
            "Brand": "HP",
            "BrandID": 1,
            "ProductRelatedLocales": [
              {
                "ID": 0,
                "Language": "EN",
                "Preferred": 0,
                "StartDate": "",
                "EndDate": ""
              }
            ]
          },
          {
            "ID": 79575992,
            "CategoryID": 1285,
            "Preferred": 0,
            "IcecatID": 1647350,
            "ProductCode": "AM863AA",
            "ThumbPic": "",
            "ProductName": "Basic Backpack",
            "Brand": "HP",
            "BrandID": 1,
            "ProductRelatedLocales": [
              {
                "ID": 0,
                "Language": "EN",
                "Preferred": 0,
                "StartDate": "",
                "EndDate": ""
              }
            ]
          },
          {
            "ID": 25218840,
            "CategoryID": 858,
            "Preferred": 0,
            "IcecatID": 1646126,
            "ProductCode": "FE477AA",
            "ThumbPic": "",
            "ProductName": "250GB Pocket Media Drive",
            "Brand": "HP",
            "BrandID": 1,
            "ProductRelatedLocales": [
              {
                "ID": 0,
                "Language": "EN",
                "Preferred": 0,
                "StartDate": "",
                "EndDate": ""
              }
            ]
          },
          {
            "ID": 79572052,
            "CategoryID": 911,
            "Preferred": 0,
            "IcecatID": 1638229,
            "ProductCode": "KT292AA",
            "ThumbPic": "",
            "ProductName": "KT292AA",
            "Brand": "HP",
            "BrandID": 1,
            "ProductRelatedLocales": [
              {
                "ID": 0,
                "Language": "EN",
                "Preferred": 0,
                "StartDate": "",
                "EndDate": ""
              }
            ]
          },
          {
            "ID": 79571323,
            "CategoryID": 911,
            "Preferred": 0,
            "IcecatID": 1638186,
            "ProductCode": "KT293AA",
            "ThumbPic": "",
            "ProductName": "KT293AA",
            "Brand": "HP",
            "BrandID": 1,
            "ProductRelatedLocales": [
              {
                "ID": 0,
                "Language": "EN",
                "Preferred": 0,
                "StartDate": "",
                "EndDate": ""
              }
            ]
          },
          {
            "ID": 79570032,
            "CategoryID": 911,
            "Preferred": 0,
            "IcecatID": 1638149,
            "ProductCode": "KT294AA",
            "ThumbPic": "",
            "ProductName": "PC2-6400 4GB",
            "Brand": "HP",
            "BrandID": 1,
            "ProductRelatedLocales": [
              {
                "ID": 0,
                "Language": "EN",
                "Preferred": 0,
                "StartDate": "",
                "EndDate": ""
              }
            ]
          },
          {
            "ID": 86513978,
            "CategoryID": 152,
            "Preferred": 0,
            "IcecatID": 1627826,
            "ProductCode": "KQ752AA",
            "ThumbPic": "",
            "ProductName": "KQ752AA",
            "Brand": "HP",
            "BrandID": 1,
            "ProductRelatedLocales": [
              {
                "ID": 0,
                "Language": "EN",
                "Preferred": 0,
                "StartDate": "",
                "EndDate": ""
              }
            ]
          },
          {
            "ID": 79566074,
            "CategoryID": 152,
            "Preferred": 0,
            "IcecatID": 1627825,
            "ProductCode": "KQ751AA",
            "ThumbPic": "",
            "ProductName": "2008 150W",
            "Brand": "HP",
            "BrandID": 1,
            "ProductRelatedLocales": [
              {
                "ID": 0,
                "Language": "EN",
                "Preferred": 0,
                "StartDate": "",
                "EndDate": ""
              }
            ]
          },
          {
            "ID": 24552089,
            "CategoryID": 152,
            "Preferred": 0,
            "IcecatID": 1627805,
            "ProductCode": "KP080AA",
            "ThumbPic": "",
            "ProductName": "2008 120W",
            "Brand": "HP",
            "BrandID": 1,
            "ProductRelatedLocales": [
              {
                "ID": 0,
                "Language": "EN",
                "Preferred": 0,
                "StartDate": "",
                "EndDate": ""
              }
            ]
          },
          {
            "ID": 86501272,
            "CategoryID": 152,
            "Preferred": 0,
            "IcecatID": 1627804,
            "ProductCode": "KP081AA",
            "ThumbPic": "",
            "ProductName": "KP081AA",
            "Brand": "HP",
            "BrandID": 1,
            "ProductRelatedLocales": [
              {
                "ID": 0,
                "Language": "EN",
                "Preferred": 0,
                "StartDate": "",
                "EndDate": ""
              }
            ]
          },
          {
            "ID": 62935462,
            "CategoryID": 2509,
            "Preferred": 0,
            "IcecatID": 1599169,
            "ProductCode": "AJ359ET",
            "ThumbPic": "",
            "ProductName": "AJ359ET",
            "Brand": "HP",
            "BrandID": 1,
            "ProductRelatedLocales": [
              {
                "ID": 0,
                "Language": "EN",
                "Preferred": 0,
                "StartDate": "",
                "EndDate": ""
              }
            ]
          },
          {
            "ID": 79560168,
            "CategoryID": 2509,
            "Preferred": 0,
            "IcecatID": 1599098,
            "ProductCode": "AJ359AA",
            "ThumbPic": "",
            "ProductName": "Extended Life Battery",
            "Brand": "HP",
            "BrandID": 1,
            "ProductRelatedLocales": [
              {
                "ID": 0,
                "Language": "EN",
                "Preferred": 0,
                "StartDate": "",
                "EndDate": ""
              }
            ]
          },
          {
            "ID": 25218842,
            "CategoryID": 827,
            "Preferred": 0,
            "IcecatID": 1587916,
            "ProductCode": "ED495ET",
            "ThumbPic": "",
            "ProductName": "90W Smart AC Adapter",
            "Brand": "HP",
            "BrandID": 1,
            "ProductRelatedLocales": [
              {
                "ID": 0,
                "Language": "EN",
                "Preferred": 0,
                "StartDate": "",
                "EndDate": ""
              }
            ]
          },
          {
            "ID": 25279278,
            "CategoryID": 803,
            "Preferred": 0,
            "IcecatID": 1570194,
            "ProductCode": "GE318T#UUW?10PCS",
            "ThumbPic": "",
            "ProductName": "Microsoft® Office Small Business 2007",
            "Brand": "HP",
            "BrandID": 1,
            "ProductRelatedLocales": [
              {
                "ID": 0,
                "Language": "EN",
                "Preferred": 0,
                "StartDate": "",
                "EndDate": ""
              }
            ]
          },
          {
            "ID": 25126129,
            "CategoryID": 911,
            "Preferred": 0,
            "IcecatID": 1547649,
            "ProductCode": "EM995ET",
            "ThumbPic": "",
            "ProductName": "DDR2-667 2GB",
            "Brand": "HP",
            "BrandID": 1,
            "ProductRelatedLocales": [
              {
                "ID": 0,
                "Language": "EN",
                "Preferred": 0,
                "StartDate": "",
                "EndDate": ""
              }
            ]
          },
          {
            "ID": 25218839,
            "CategoryID": 219,
            "Preferred": 0,
            "IcecatID": 1454607,
            "ProductCode": "AK072AA",
            "ThumbPic": "",
            "ProductName": "250-GB 5400rpm Primary SATA Hard Drive",
            "Brand": "HP",
            "BrandID": 1,
            "ProductRelatedLocales": [
              {
                "ID": 0,
                "Language": "EN",
                "Preferred": 0,
                "StartDate": "",
                "EndDate": ""
              }
            ]
          },
          {
            "ID": 21918434,
            "CategoryID": 152,
            "Preferred": 0,
            "IcecatID": 1441890,
            "ProductCode": "EN488ET#ABB/KIT2",
            "ThumbPic": "",
            "ProductName": "Basic Docking Station with Smart AC Adapter",
            "Brand": "HP",
            "BrandID": 1,
            "ProductRelatedLocales": [
              {
                "ID": 0,
                "Language": "EN",
                "Preferred": 0,
                "StartDate": "",
                "EndDate": ""
              }
            ]
          },
          {
            "ID": 22987978,
            "CategoryID": 152,
            "Preferred": 0,
            "IcecatID": 1441889,
            "ProductCode": "EN489ET#ABB/KIT",
            "ThumbPic": "",
            "ProductName": "Advanced Docking Station",
            "Brand": "HP",
            "BrandID": 1,
            "ProductRelatedLocales": [
              {
                "ID": 0,
                "Language": "EN",
                "Preferred": 0,
                "StartDate": "",
                "EndDate": ""
              }
            ]
          },
          {
            "ID": 21918433,
            "CategoryID": 152,
            "Preferred": 0,
            "IcecatID": 1441886,
            "ProductCode": "EN488ET#ABB/KIT3",
            "ThumbPic": "",
            "ProductName": "Basic Docking Station with Smart AC Adapter",
            "Brand": "HP",
            "BrandID": 1,
            "ProductRelatedLocales": [
              {
                "ID": 0,
                "Language": "EN",
                "Preferred": 0,
                "StartDate": "",
                "EndDate": ""
              }
            ]
          },
          {
            "ID": 21918392,
            "CategoryID": 152,
            "Preferred": 0,
            "IcecatID": 1370761,
            "ProductCode": "PA508A#*PERFECT",
            "ThumbPic": "",
            "ProductName": "Adjustable Notebook Stand",
            "Brand": "HP",
            "BrandID": 1,
            "ProductRelatedLocales": [
              {
                "ID": 0,
                "Language": "EN",
                "Preferred": 0,
                "StartDate": "",
                "EndDate": ""
              }
            ]
          },
          {
            "ID": 21918436,
            "CategoryID": 195,
            "Preferred": 0,
            "IcecatID": 1370516,
            "ProductCode": "RJ316AA#*MOBILE",
            "ThumbPic": "",
            "ProductName": "Bluetooth PC Card Mouse",
            "Brand": "HP",
            "BrandID": 1,
            "ProductRelatedLocales": [
              {
                "ID": 0,
                "Language": "EN",
                "Preferred": 0,
                "StartDate": "",
                "EndDate": ""
              }
            ]
          },
          {
            "ID": 21918444,
            "CategoryID": 822,
            "Preferred": 0,
            "IcecatID": 1370456,
            "ProductCode": "RR315AA#*BASIC",
            "ThumbPic": "",
            "ProductName": "Universal Nylon Case",
            "Brand": "HP",
            "BrandID": 1,
            "ProductRelatedLocales": [
              {
                "ID": 0,
                "Language": "EN",
                "Preferred": 0,
                "StartDate": "",
                "EndDate": ""
              }
            ]
          },
          {
            "ID": 21918432,
            "CategoryID": 152,
            "Preferred": 0,
            "IcecatID": 1362587,
            "ProductCode": "EN488ET#ABB+RR314ET",
            "ThumbPic": "",
            "ProductName": "Basic Docking Station with Smart AC Adapter",
            "Brand": "HP",
            "BrandID": 1,
            "ProductRelatedLocales": [
              {
                "ID": 0,
                "Language": "EN",
                "Preferred": 0,
                "StartDate": "",
                "EndDate": ""
              }
            ]
          },
          {
            "ID": 25279276,
            "CategoryID": 803,
            "Preferred": 0,
            "IcecatID": 1361272,
            "ProductCode": "GE318T#UUW+RR314ET",
            "ThumbPic": "",
            "ProductName": "Microsoft® Office Small Business 2007",
            "Brand": "HP",
            "BrandID": 1,
            "ProductRelatedLocales": [
              {
                "ID": 0,
                "Language": "EN",
                "Preferred": 0,
                "StartDate": "",
                "EndDate": ""
              }
            ]
          },
          {
            "ID": 48885600,
            "CategoryID": 152,
            "Preferred": 0,
            "IcecatID": 1361130,
            "ProductCode": "EN488ET#ABB+RR314ET+GE318T",
            "ThumbPic": "",
            "ProductName": "Basic Docking Station with Smart AC Adapter",
            "Brand": "HP",
            "BrandID": 1,
            "ProductRelatedLocales": [
              {
                "ID": 0,
                "Language": "EN",
                "Preferred": 0,
                "StartDate": "",
                "EndDate": ""
              }
            ]
          },
          {
            "ID": 79536533,
            "CategoryID": 943,
            "Preferred": 0,
            "IcecatID": 1354212,
            "ProductCode": "AJ358AA",
            "ThumbPic": "",
            "ProductName": "15.4-inch Display Privacy Filter",
            "Brand": "HP",
            "BrandID": 1,
            "ProductRelatedLocales": [
              {
                "ID": 0,
                "Language": "EN",
                "Preferred": 0,
                "StartDate": "",
                "EndDate": ""
              }
            ]
          },
          {
            "ID": 127959192,
            "CategoryID": 1514,
            "Preferred": 0,
            "IcecatID": 1351682,
            "ProductCode": "NOTEBOOK-D100",
            "ThumbPic": "",
            "ProductName": "Neomounts by Newstar laptop desk mount",
            "Brand": "Neomounts by Newstar",
            "BrandID": 290,
            "ProductRelatedLocales": [
              {
                "ID": 0,
                "Language": "EN",
                "Preferred": 0,
                "StartDate": "",
                "EndDate": ""
              }
            ]
          },
          {
            "ID": 64279591,
            "CategoryID": 803,
            "Preferred": 0,
            "IcecatID": 1347086,
            "ProductCode": "RZ362A#ABH",
            "ThumbPic": "",
            "ProductName": "Microsoft Office Basic 2007 Activation License - HP Media-less License",
            "Brand": "HP",
            "BrandID": 1,
            "ProductRelatedLocales": [
              {
                "ID": 0,
                "Language": "EN",
                "Preferred": 0,
                "StartDate": "",
                "EndDate": ""
              }
            ]
          },
          {
            "ID": 24552134,
            "CategoryID": 194,
            "Preferred": 0,
            "IcecatID": 1334912,
            "ProductCode": "DT528A#AB9?C",
            "ThumbPic": "",
            "ProductName": " Standard Basic Keyboard 2004 USB",
            "Brand": "HP",
            "BrandID": 1,
            "ProductRelatedLocales": [
              {
                "ID": 0,
                "Language": "EN",
                "Preferred": 0,
                "StartDate": "",
                "EndDate": ""
              }
            ]
          },
          {
            "ID": 21918430,
            "CategoryID": 152,
            "Preferred": 0,
            "IcecatID": 1333403,
            "ProductCode": "EN488ET#ABB/KIT1",
            "ThumbPic": "",
            "ProductName": "Basic Docking Station with Smart AC Adapter",
            "Brand": "HP",
            "BrandID": 1,
            "ProductRelatedLocales": [
              {
                "ID": 0,
                "Language": "EN",
                "Preferred": 0,
                "StartDate": "",
                "EndDate": ""
              }
            ]
          },
          {
            "ID": 21918412,
            "CategoryID": 814,
            "Preferred": 0,
            "IcecatID": 1333401,
            "ProductCode": "EJ092AA#B13/KIT2",
            "ThumbPic": "",
            "ProductName": "Ultra-Capacity Battery",
            "Brand": "HP",
            "BrandID": 1,
            "ProductRelatedLocales": [
              {
                "ID": 0,
                "Language": "EN",
                "Preferred": 0,
                "StartDate": "",
                "EndDate": ""
              }
            ]
          },
          {
            "ID": 25279285,
            "CategoryID": 803,
            "Preferred": 0,
            "IcecatID": 1319327,
            "ProductCode": "GE316T#UUW_X",
            "ThumbPic": "",
            "ProductName": "Microsoft® Office Basic Edition 2007",
            "Brand": "HP",
            "BrandID": 1,
            "ProductRelatedLocales": [
              {
                "ID": 0,
                "Language": "EN",
                "Preferred": 0,
                "StartDate": "",
                "EndDate": ""
              }
            ]
          },
          {
            "ID": 50470326,
            "CategoryID": 829,
            "Preferred": 0,
            "IcecatID": 1313285,
            "ProductCode": "RW635AA#AC3",
            "ThumbPic": "",
            "ProductName": "1-Bay Battery Charging Station",
            "Brand": "HP",
            "BrandID": 1,
            "ProductRelatedLocales": [
              {
                "ID": 0,
                "Language": "EN",
                "Preferred": 0,
                "StartDate": "",
                "EndDate": ""
              }
            ]
          },
          {
            "ID": 24552133,
            "CategoryID": 194,
            "Preferred": 0,
            "IcecatID": 1306049,
            "ProductCode": "DT528A#ABZ--OT",
            "ThumbPic": "",
            "ProductName": "Standard Basic Keyboard 2004 USB",
            "Brand": "HP",
            "BrandID": 1,
            "ProductRelatedLocales": [
              {
                "ID": 0,
                "Language": "EN",
                "Preferred": 0,
                "StartDate": "",
                "EndDate": ""
              }
            ]
          },
          {
            "ID": 24552132,
            "CategoryID": 194,
            "Preferred": 0,
            "IcecatID": 1306045,
            "ProductCode": "DT528A#ABE--OT",
            "ThumbPic": "",
            "ProductName": "Standard Basic Keyboard 2004 USB",
            "Brand": "HP",
            "BrandID": 1,
            "ProductRelatedLocales": [
              {
                "ID": 0,
                "Language": "EN",
                "Preferred": 0,
                "StartDate": "",
                "EndDate": ""
              }
            ]
          },
          {
            "ID": 48886055,
            "CategoryID": 1285,
            "Preferred": 0,
            "IcecatID": 1241360,
            "ProductCode": "AJ078AA",
            "ThumbPic": "",
            "ProductName": "AJ078AA",
            "Brand": "HP",
            "BrandID": 1,
            "ProductRelatedLocales": [
              {
                "ID": 0,
                "Language": "EN",
                "Preferred": 0,
                "StartDate": "",
                "EndDate": ""
              }
            ]
          },
          {
            "ID": 48886045,
            "CategoryID": 1170,
            "Preferred": 0,
            "IcecatID": 1230814,
            "ProductCode": "RW635AA",
            "ThumbPic": "",
            "ProductName": "1-Bay Battery Charging Station",
            "Brand": "HP",
            "BrandID": 1,
            "ProductRelatedLocales": [
              {
                "ID": 0,
                "Language": "EN",
                "Preferred": 0,
                "StartDate": "",
                "EndDate": ""
              }
            ]
          },
          {
            "ID": 48886040,
            "CategoryID": 219,
            "Preferred": 0,
            "IcecatID": 1230805,
            "ProductCode": "AH920AA",
            "ThumbPic": "",
            "ProductName": "120-GB 7200rpm Primary SATA Hard Drive",
            "Brand": "HP",
            "BrandID": 1,
            "ProductRelatedLocales": [
              {
                "ID": 0,
                "Language": "EN",
                "Preferred": 0,
                "StartDate": "",
                "EndDate": ""
              }
            ]
          },
          {
            "ID": 48885555,
            "CategoryID": 827,
            "Preferred": 0,
            "IcecatID": 1200354,
            "ProductCode": "ED993AA",
            "ThumbPic": "",
            "ProductName": "ED993AA",
            "Brand": "HP",
            "BrandID": 1,
            "ProductRelatedLocales": [
              {
                "ID": 0,
                "Language": "EN",
                "Preferred": 0,
                "StartDate": "",
                "EndDate": ""
              }
            ]
          },
          {
            "ID": 22987974,
            "CategoryID": 152,
            "Preferred": 0,
            "IcecatID": 1200099,
            "ProductCode": "EN488AA",
            "ThumbPic": "",
            "ProductName": "Docking Station with Smart Adapter",
            "Brand": "HP",
            "BrandID": 1,
            "ProductRelatedLocales": [
              {
                "ID": 0,
                "Language": "EN",
                "Preferred": 0,
                "StartDate": "",
                "EndDate": ""
              }
            ]
          },
          {
            "ID": 64271218,
            "CategoryID": 803,
            "Preferred": 0,
            "IcecatID": 919432,
            "ProductCode": "RZ362A",
            "ThumbPic": "",
            "ProductName": "Microsoft Office Basic 2007 Activation License - HP Media-less License",
            "Brand": "HP",
            "BrandID": 1,
            "ProductRelatedLocales": [
              {
                "ID": 0,
                "Language": "EN",
                "Preferred": 0,
                "StartDate": "",
                "EndDate": ""
              }
            ]
          },
          {
            "ID": 25279310,
            "CategoryID": 803,
            "Preferred": 0,
            "IcecatID": 906567,
            "ProductCode": "RZ366A",
            "ThumbPic": "",
            "ProductName": "Microsoft Office Small Business 2007 Activation License - Media-less License",
            "Brand": "HP",
            "BrandID": 1,
            "ProductRelatedLocales": [
              {
                "ID": 0,
                "Language": "EN",
                "Preferred": 0,
                "StartDate": "",
                "EndDate": ""
              }
            ]
          },
          {
            "ID": 25279308,
            "CategoryID": 1523,
            "Preferred": 0,
            "IcecatID": 887068,
            "ProductCode": "RZ366A#ABH",
            "ThumbPic": "",
            "ProductName": "Microsoft Office Small Business 2007 Activation License - HP Media-less License",
            "Brand": "HP",
            "BrandID": 1,
            "ProductRelatedLocales": [
              {
                "ID": 0,
                "Language": "EN",
                "Preferred": 0,
                "StartDate": "",
                "EndDate": ""
              }
            ]
          },
          {
            "ID": 21918429,
            "CategoryID": 152,
            "Preferred": 0,
            "IcecatID": 880676,
            "ProductCode": "EN488ET#ABB/KIT",
            "ThumbPic": "",
            "ProductName": "Basic Docking Station with Smart AC Adapter",
            "Brand": "HP",
            "BrandID": 1,
            "ProductRelatedLocales": [
              {
                "ID": 0,
                "Language": "EN",
                "Preferred": 0,
                "StartDate": "",
                "EndDate": ""
              }
            ]
          },
          {
            "ID": 21918341,
            "CategoryID": 194,
            "Preferred": 0,
            "IcecatID": 879597,
            "ProductCode": "DT527A#ABZ#*AGFA*#",
            "ThumbPic": "",
            "ProductName": "Standard Basic Keyboard 2004 PS2",
            "Brand": "HP",
            "BrandID": 1,
            "ProductRelatedLocales": [
              {
                "ID": 0,
                "Language": "EN",
                "Preferred": 0,
                "StartDate": "",
                "EndDate": ""
              }
            ]
          },
          {
            "ID": 21918340,
            "CategoryID": 194,
            "Preferred": 0,
            "IcecatID": 879595,
            "ProductCode": "DT527A#AC0#*AGFA",
            "ThumbPic": "",
            "ProductName": "Standard Basic Keyboard 2004 PS2",
            "Brand": "HP",
            "BrandID": 1,
            "ProductRelatedLocales": [
              {
                "ID": 0,
                "Language": "EN",
                "Preferred": 0,
                "StartDate": "",
                "EndDate": ""
              }
            ]
          },
          {
            "ID": 21918339,
            "CategoryID": 194,
            "Preferred": 0,
            "IcecatID": 879564,
            "ProductCode": "DT527A#AB9#*AGFA",
            "ThumbPic": "",
            "ProductName": "Standard Basic Keyboard 2004 PS2",
            "Brand": "HP",
            "BrandID": 1,
            "ProductRelatedLocales": [
              {
                "ID": 0,
                "Language": "EN",
                "Preferred": 0,
                "StartDate": "",
                "EndDate": ""
              }
            ]
          },
          {
            "ID": 23258675,
            "CategoryID": 211,
            "Preferred": 0,
            "IcecatID": 879560,
            "ProductCode": "DC361B#*AGFA",
            "ThumbPic": "",
            "ProductName": "USB Floppy Disk Drive, External",
            "Brand": "HP",
            "BrandID": 1,
            "ProductRelatedLocales": [
              {
                "ID": 0,
                "Language": "EN",
                "Preferred": 0,
                "StartDate": "",
                "EndDate": ""
              }
            ]
          },
          {
            "ID": 21918338,
            "CategoryID": 194,
            "Preferred": 0,
            "IcecatID": 879494,
            "ProductCode": "DT527A#ABU#*AGFA-HC",
            "ThumbPic": "",
            "ProductName": "Standard Basic Keyboard 2004 PS2",
            "Brand": "HP",
            "BrandID": 1,
            "ProductRelatedLocales": [
              {
                "ID": 0,
                "Language": "EN",
                "Preferred": 0,
                "StartDate": "",
                "EndDate": ""
              }
            ]
          },
          {
            "ID": 21918337,
            "CategoryID": 194,
            "Preferred": 0,
            "IcecatID": 879442,
            "ProductCode": "DT527A#ABD#*AGFA-HC",
            "ThumbPic": "",
            "ProductName": "Standard Basic Keyboard 2004 PS2",
            "Brand": "HP",
            "BrandID": 1,
            "ProductRelatedLocales": [
              {
                "ID": 0,
                "Language": "EN",
                "Preferred": 0,
                "StartDate": "",
                "EndDate": ""
              }
            ]
          },
          {
            "ID": 21918336,
            "CategoryID": 194,
            "Preferred": 0,
            "IcecatID": 879439,
            "ProductCode": "DT527A#ABB#*AGFA",
            "ThumbPic": "",
            "ProductName": "Standard Basic Keyboard 2004 PS2",
            "Brand": "HP",
            "BrandID": 1,
            "ProductRelatedLocales": [
              {
                "ID": 0,
                "Language": "EN",
                "Preferred": 0,
                "StartDate": "",
                "EndDate": ""
              }
            ]
          },
          {
            "ID": 21918335,
            "CategoryID": 194,
            "Preferred": 0,
            "IcecatID": 879414,
            "ProductCode": "DT527A#ABE#*AGFA",
            "ThumbPic": "",
            "ProductName": "Standard Basic Keyboard 2004 PS2",
            "Brand": "HP",
            "BrandID": 1,
            "ProductRelatedLocales": [
              {
                "ID": 0,
                "Language": "EN",
                "Preferred": 0,
                "StartDate": "",
                "EndDate": ""
              }
            ]
          },
          {
            "ID": 21918334,
            "CategoryID": 194,
            "Preferred": 0,
            "IcecatID": 879401,
            "ProductCode": "DT527A#ABD#*AGFA",
            "ThumbPic": "",
            "ProductName": "Standard Basic Keyboard 2004 PS2",
            "Brand": "HP",
            "BrandID": 1,
            "ProductRelatedLocales": [
              {
                "ID": 0,
                "Language": "EN",
                "Preferred": 0,
                "StartDate": "",
                "EndDate": ""
              }
            ]
          },
          {
            "ID": 21918333,
            "CategoryID": 194,
            "Preferred": 0,
            "IcecatID": 879395,
            "ProductCode": "DT527A#ABS#*AGFA-HC",
            "ThumbPic": "",
            "ProductName": "Standard Basic Keyboard 2004 PS2",
            "Brand": "HP",
            "BrandID": 1,
            "ProductRelatedLocales": [
              {
                "ID": 0,
                "Language": "EN",
                "Preferred": 0,
                "StartDate": "",
                "EndDate": ""
              }
            ]
          },
          {
            "ID": 21918332,
            "CategoryID": 194,
            "Preferred": 0,
            "IcecatID": 879390,
            "ProductCode": "DT527A#ABF#*AGFA*#",
            "ThumbPic": "",
            "ProductName": "Standard Basic Keyboard 2004 PS2",
            "Brand": "HP",
            "BrandID": 1,
            "ProductRelatedLocales": [
              {
                "ID": 0,
                "Language": "EN",
                "Preferred": 0,
                "StartDate": "",
                "EndDate": ""
              }
            ]
          },
          {
            "ID": 21918331,
            "CategoryID": 194,
            "Preferred": 0,
            "IcecatID": 879374,
            "ProductCode": "DT527A#AB8#*AGFA-HC",
            "ThumbPic": "",
            "ProductName": "Standard Basic Keyboard 2004 PS2",
            "Brand": "HP",
            "BrandID": 1,
            "ProductRelatedLocales": [
              {
                "ID": 0,
                "Language": "EN",
                "Preferred": 0,
                "StartDate": "",
                "EndDate": ""
              }
            ]
          },
          {
            "ID": 21918330,
            "CategoryID": 194,
            "Preferred": 0,
            "IcecatID": 879364,
            "ProductCode": "DT527A#ABH#*AGFA-HC",
            "ThumbPic": "",
            "ProductName": "Standard Basic Keyboard 2004 PS2",
            "Brand": "HP",
            "BrandID": 1,
            "ProductRelatedLocales": [
              {
                "ID": 0,
                "Language": "EN",
                "Preferred": 0,
                "StartDate": "",
                "EndDate": ""
              }
            ]
          },
          {
            "ID": 21918329,
            "CategoryID": 194,
            "Preferred": 0,
            "IcecatID": 879358,
            "ProductCode": "DT527A#ABY#*AGFA",
            "ThumbPic": "",
            "ProductName": "Standard Basic Keyboard 2004 PS2",
            "Brand": "HP",
            "BrandID": 1,
            "ProductRelatedLocales": [
              {
                "ID": 0,
                "Language": "EN",
                "Preferred": 0,
                "StartDate": "",
                "EndDate": ""
              }
            ]
          },
          {
            "ID": 21918328,
            "CategoryID": 194,
            "Preferred": 0,
            "IcecatID": 879349,
            "ProductCode": "DT527A#ABN#*AGFA",
            "ThumbPic": "",
            "ProductName": "Standard Basic Keyboard 2004 PS2",
            "Brand": "HP",
            "BrandID": 1,
            "ProductRelatedLocales": [
              {
                "ID": 0,
                "Language": "EN",
                "Preferred": 0,
                "StartDate": "",
                "EndDate": ""
              }
            ]
          },
          {
            "ID": 79499131,
            "CategoryID": 803,
            "Preferred": 0,
            "IcecatID": 867101,
            "ProductCode": "RZ364A",
            "ThumbPic": "",
            "ProductName": "Microsoft Office Professional 2007 Activation License - HP Media-less License",
            "Brand": "HP",
            "BrandID": 1,
            "ProductRelatedLocales": [
              {
                "ID": 0,
                "Language": "EN",
                "Preferred": 0,
                "StartDate": "",
                "EndDate": ""
              }
            ]
          },
          {
            "ID": 21918428,
            "CategoryID": 152,
            "Preferred": 0,
            "IcecatID": 866918,
            "ProductCode": "EN488ET#30895074",
            "ThumbPic": "",
            "ProductName": "Basic Docking Station with Smart AC Adapter",
            "Brand": "HP",
            "BrandID": 1,
            "ProductRelatedLocales": [
              {
                "ID": 0,
                "Language": "EN",
                "Preferred": 0,
                "StartDate": "",
                "EndDate": ""
              }
            ]
          },
          {
            "ID": 21918442,
            "CategoryID": 195,
            "Preferred": 0,
            "IcecatID": 866916,
            "ProductCode": "RH304AA#30895091",
            "ThumbPic": "",
            "ProductName": "USB Optical Travel Mouse",
            "Brand": "HP",
            "BrandID": 1,
            "ProductRelatedLocales": [
              {
                "ID": 0,
                "Language": "EN",
                "Preferred": 0,
                "StartDate": "",
                "EndDate": ""
              }
            ]
          },
          {
            "ID": 22987968,
            "CategoryID": 814,
            "Preferred": 0,
            "IcecatID": 866915,
            "ProductCode": "PB993ET#30895081",
            "ThumbPic": "",
            "ProductName": "Extended Life Battery",
            "Brand": "HP",
            "BrandID": 1,
            "ProductRelatedLocales": [
              {
                "ID": 0,
                "Language": "EN",
                "Preferred": 0,
                "StartDate": "",
                "EndDate": ""
              }
            ]
          },
          {
            "ID": 25279273,
            "CategoryID": 803,
            "Preferred": 0,
            "IcecatID": 866905,
            "ProductCode": "GE318T#30895113",
            "ThumbPic": "",
            "ProductName": "Microsoft® Office Small Business 2007",
            "Brand": "HP",
            "BrandID": 1,
            "ProductRelatedLocales": [
              {
                "ID": 0,
                "Language": "EN",
                "Preferred": 0,
                "StartDate": "",
                "EndDate": ""
              }
            ]
          },
          {
            "ID": 21918326,
            "CategoryID": 194,
            "Preferred": 0,
            "IcecatID": 855136,
            "ProductCode": "DT527A#ABS#*AGFA",
            "ThumbPic": "",
            "ProductName": "Standard Basic Keyboard 2004 PS2",
            "Brand": "HP",
            "BrandID": 1,
            "ProductRelatedLocales": [
              {
                "ID": 0,
                "Language": "EN",
                "Preferred": 0,
                "StartDate": "",
                "EndDate": ""
              }
            ]
          },
          {
            "ID": 25279279,
            "CategoryID": 803,
            "Preferred": 0,
            "IcecatID": 849972,
            "ProductCode": "GE316T",
            "ThumbPic": "",
            "ProductName": "Microsoft Office Basic 2007 Activation License - Media-less License",
            "Brand": "HP",
            "BrandID": 1,
            "ProductRelatedLocales": [
              {
                "ID": 0,
                "Language": "EN",
                "Preferred": 0,
                "StartDate": "",
                "EndDate": ""
              }
            ]
          },
          {
            "ID": 78472230,
            "CategoryID": 1285,
            "Preferred": 0,
            "IcecatID": 836007,
            "ProductCode": "RR317ET",
            "ThumbPic": "",
            "ProductName": "RR317ET",
            "Brand": "HP",
            "BrandID": 1,
            "ProductRelatedLocales": [
              {
                "ID": 0,
                "Language": "EN",
                "Preferred": 0,
                "StartDate": "",
                "EndDate": ""
              }
            ]
          },
          {
            "ID": 21918427,
            "CategoryID": 152,
            "Preferred": 0,
            "IcecatID": 835244,
            "ProductCode": "EN488ET#ABB#*ATKIT",
            "ThumbPic": "",
            "ProductName": "Basic Docking Station with Smart AC Adapter",
            "Brand": "HP",
            "BrandID": 1,
            "ProductRelatedLocales": [
              {
                "ID": 0,
                "Language": "EN",
                "Preferred": 0,
                "StartDate": "",
                "EndDate": ""
              }
            ]
          },
          {
            "ID": 25279282,
            "CategoryID": 803,
            "Preferred": 0,
            "IcecatID": 832779,
            "ProductCode": "GE316T#ABH",
            "ThumbPic": "",
            "ProductName": "Microsoft Office Basic 2007 Activation License - HP Media-less License",
            "Brand": "HP",
            "BrandID": 1,
            "ProductRelatedLocales": [
              {
                "ID": 0,
                "Language": "EN",
                "Preferred": 0,
                "StartDate": "",
                "EndDate": ""
              }
            ]
          },
          {
            "ID": 63795143,
            "CategoryID": 803,
            "Preferred": 0,
            "IcecatID": 832778,
            "ProductCode": "GE317T#ABH",
            "ThumbPic": "",
            "ProductName": "Microsoft Office Professional 2007 Activation License - HP Media-less License",
            "Brand": "HP",
            "BrandID": 1,
            "ProductRelatedLocales": [
              {
                "ID": 0,
                "Language": "EN",
                "Preferred": 0,
                "StartDate": "",
                "EndDate": ""
              }
            ]
          },
          {
            "ID": 64202113,
            "CategoryID": 803,
            "Preferred": 0,
            "IcecatID": 832777,
            "ProductCode": "GE318T#ABH",
            "ThumbPic": "",
            "ProductName": "Microsoft Office Small Business 2007 Activation License - HP Media-less License",
            "Brand": "HP",
            "BrandID": 1,
            "ProductRelatedLocales": [
              {
                "ID": 0,
                "Language": "EN",
                "Preferred": 0,
                "StartDate": "",
                "EndDate": ""
              }
            ]
          },
          {
            "ID": 63821114,
            "CategoryID": 803,
            "Preferred": 0,
            "IcecatID": 832540,
            "ProductCode": "GE317T",
            "ThumbPic": "",
            "ProductName": "Microsoft Office Professional 2007 Activation License - HP Media-less License",
            "Brand": "HP",
            "BrandID": 1,
            "ProductRelatedLocales": [
              {
                "ID": 0,
                "Language": "EN",
                "Preferred": 0,
                "StartDate": "",
                "EndDate": ""
              }
            ]
          },
          {
            "ID": 48885820,
            "CategoryID": 1285,
            "Preferred": 0,
            "IcecatID": 831975,
            "ProductCode": "RR314ET",
            "ThumbPic": "",
            "ProductName": "Value Nylon Case",
            "Brand": "HP",
            "BrandID": 1,
            "ProductRelatedLocales": [
              {
                "ID": 0,
                "Language": "EN",
                "Preferred": 0,
                "StartDate": "",
                "EndDate": ""
              }
            ]
          },
          {
            "ID": 64225840,
            "CategoryID": 803,
            "Preferred": 0,
            "IcecatID": 830601,
            "ProductCode": "GE318T",
            "ThumbPic": "",
            "ProductName": "Microsoft Office Small Business 2007 Activation License - HP Media-less License",
            "Brand": "HP",
            "BrandID": 1,
            "ProductRelatedLocales": [
              {
                "ID": 0,
                "Language": "EN",
                "Preferred": 0,
                "StartDate": "",
                "EndDate": ""
              }
            ]
          },
          {
            "ID": 21918426,
            "CategoryID": 152,
            "Preferred": 0,
            "IcecatID": 798846,
            "ProductCode": "EN488ET#ABB-DEMO2",
            "ThumbPic": "",
            "ProductName": "Basic Docking Station with Smart AC Adapter",
            "Brand": "HP",
            "BrandID": 1,
            "ProductRelatedLocales": [
              {
                "ID": 0,
                "Language": "EN",
                "Preferred": 0,
                "StartDate": "",
                "EndDate": ""
              }
            ]
          },
          {
            "ID": 48885645,
            "CategoryID": 1285,
            "Preferred": 0,
            "IcecatID": 797912,
            "ProductCode": "RR314AA",
            "ThumbPic": "",
            "ProductName": "RR314AA",
            "Brand": "HP",
            "BrandID": 1,
            "ProductRelatedLocales": [
              {
                "ID": 0,
                "Language": "EN",
                "Preferred": 0,
                "StartDate": "",
                "EndDate": ""
              }
            ]
          },
          {
            "ID": 50470172,
            "CategoryID": 1285,
            "Preferred": 0,
            "IcecatID": 797879,
            "ProductCode": "RR315AA",
            "ThumbPic": "",
            "ProductName": "RR315AA",
            "Brand": "HP",
            "BrandID": 1,
            "ProductRelatedLocales": [
              {
                "ID": 0,
                "Language": "EN",
                "Preferred": 0,
                "StartDate": "",
                "EndDate": ""
              }
            ]
          },
          {
            "ID": 48885650,
            "CategoryID": 1285,
            "Preferred": 0,
            "IcecatID": 797852,
            "ProductCode": "RR317AA",
            "ThumbPic": "",
            "ProductName": "RR317AA",
            "Brand": "HP",
            "BrandID": 1,
            "ProductRelatedLocales": [
              {
                "ID": 0,
                "Language": "EN",
                "Preferred": 0,
                "StartDate": "",
                "EndDate": ""
              }
            ]
          },
          {
            "ID": 23400270,
            "CategoryID": 152,
            "Preferred": 0,
            "IcecatID": 788096,
            "ProductCode": "EM537AA",
            "ThumbPic": "",
            "ProductName": "3-in-1 NAS Docking Station",
            "Brand": "HP",
            "BrandID": 1,
            "ProductRelatedLocales": [
              {
                "ID": 0,
                "Language": "EN",
                "Preferred": 0,
                "StartDate": "",
                "EndDate": ""
              }
            ]
          },
          {
            "ID": 70348960,
            "CategoryID": 219,
            "Preferred": 0,
            "IcecatID": 688897,
            "ProductCode": "RT080AA",
            "ThumbPic": "",
            "ProductName": "120GB 5400rpm Primary SATA Hard Drive",
            "Brand": "HP",
            "BrandID": 1,
            "ProductRelatedLocales": [
              {
                "ID": 0,
                "Language": "EN",
                "Preferred": 0,
                "StartDate": "",
                "EndDate": ""
              }
            ]
          },
          {
            "ID": 24552080,
            "CategoryID": 195,
            "Preferred": 0,
            "IcecatID": 659840,
            "ProductCode": "RJ316ET",
            "ThumbPic": "",
            "ProductName": "RJ316ET",
            "Brand": "HP",
            "BrandID": 1,
            "ProductRelatedLocales": [
              {
                "ID": 0,
                "Language": "EN",
                "Preferred": 0,
                "StartDate": "",
                "EndDate": ""
              }
            ]
          },
          {
            "ID": 48885635,
            "CategoryID": 195,
            "Preferred": 0,
            "IcecatID": 653721,
            "ProductCode": "RH304AA",
            "ThumbPic": "",
            "ProductName": "RH304AA",
            "Brand": "HP",
            "BrandID": 1,
            "ProductRelatedLocales": [
              {
                "ID": 0,
                "Language": "EN",
                "Preferred": 0,
                "StartDate": "",
                "EndDate": ""
              }
            ]
          },
          {
            "ID": 21918410,
            "CategoryID": 814,
            "Preferred": 0,
            "IcecatID": 630851,
            "ProductCode": "EJ092AA#B13/KIT1",
            "ThumbPic": "",
            "ProductName": "Ultra-Capacity Battery",
            "Brand": "HP",
            "BrandID": 1,
            "ProductRelatedLocales": [
              {
                "ID": 0,
                "Language": "EN",
                "Preferred": 0,
                "StartDate": "",
                "EndDate": ""
              }
            ]
          },
          {
            "ID": 21918425,
            "CategoryID": 152,
            "Preferred": 0,
            "IcecatID": 584774,
            "ProductCode": "EN488ET#ABB+EM869AT",
            "ThumbPic": "",
            "ProductName": "Basic Docking Station with Smart AC Adapter",
            "Brand": "HP",
            "BrandID": 1,
            "ProductRelatedLocales": [
              {
                "ID": 0,
                "Language": "EN",
                "Preferred": 0,
                "StartDate": "",
                "EndDate": ""
              }
            ]
          },
          {
            "ID": 24552125,
            "CategoryID": 194,
            "Preferred": 0,
            "IcecatID": 572163,
            "ProductCode": "DT528A#ABY-D30",
            "ThumbPic": "",
            "ProductName": "Standard Basic Keyboard 2004 USB",
            "Brand": "HP",
            "BrandID": 1,
            "ProductRelatedLocales": [
              {
                "ID": 0,
                "Language": "EN",
                "Preferred": 0,
                "StartDate": "",
                "EndDate": ""
              }
            ]
          },
          {
            "ID": 21918408,
            "CategoryID": 814,
            "Preferred": 0,
            "IcecatID": 559588,
            "ProductCode": "EJ092AA#B13/KIT",
            "ThumbPic": "",
            "ProductName": "Ultra-Capacity Battery",
            "Brand": "HP",
            "BrandID": 1,
            "ProductRelatedLocales": [
              {
                "ID": 0,
                "Language": "EN",
                "Preferred": 0,
                "StartDate": "",
                "EndDate": ""
              }
            ]
          },
          {
            "ID": 147689761,
            "CategoryID": 911,
            "Preferred": 0,
            "IcecatID": 558345,
            "ProductCode": "KTH-ZD8000B/2G",
            "ThumbPic": "",
            "ProductName": "2GB DDR2-667",
            "Brand": "Kingston Technology",
            "BrandID": 18,
            "ProductRelatedLocales": [
              {
                "ID": 0,
                "Language": "EN",
                "Preferred": 0,
                "StartDate": "",
                "EndDate": ""
              }
            ]
          },
          {
            "ID": 134002699,
            "CategoryID": 194,
            "Preferred": 0,
            "IcecatID": 557179,
            "ProductCode": "DT528A",
            "ThumbPic": "",
            "ProductName": "USB Standard Keyboard",
            "Brand": "HP",
            "BrandID": 1,
            "ProductRelatedLocales": [
              {
                "ID": 0,
                "Language": "EN",
                "Preferred": 0,
                "StartDate": "",
                "EndDate": ""
              }
            ]
          },
          {
            "ID": 24552121,
            "CategoryID": 194,
            "Preferred": 0,
            "IcecatID": 549304,
            "ProductCode": "DT528A#ABU#*AGFA-HC",
            "ThumbPic": "",
            "ProductName": "Standard Basic Keyboard 2004 USB",
            "Brand": "HP",
            "BrandID": 1,
            "ProductRelatedLocales": [
              {
                "ID": 0,
                "Language": "EN",
                "Preferred": 0,
                "StartDate": "",
                "EndDate": ""
              }
            ]
          },
          {
            "ID": 48885521,
            "CategoryID": 827,
            "Preferred": 0,
            "IcecatID": 509090,
            "ProductCode": "ED495AA",
            "ThumbPic": "",
            "ProductName": "90W Smart AC Adapter",
            "Brand": "HP",
            "BrandID": 1,
            "ProductRelatedLocales": [
              {
                "ID": 0,
                "Language": "EN",
                "Preferred": 0,
                "StartDate": "",
                "EndDate": ""
              }
            ]
          },
          {
            "ID": 48885610,
            "CategoryID": 1754,
            "Preferred": 0,
            "IcecatID": 483744,
            "ProductCode": "EL348AA",
            "ThumbPic": "",
            "ProductName": "ProtectTools (10 units) Java Cards",
            "Brand": "HP",
            "BrandID": 1,
            "ProductRelatedLocales": [
              {
                "ID": 0,
                "Language": "EN",
                "Preferred": 0,
                "StartDate": "",
                "EndDate": ""
              }
            ]
          },
          {
            "ID": 26874861,
            "CategoryID": 788,
            "Preferred": 0,
            "IcecatID": 483534,
            "ProductCode": "UE323A",
            "ThumbPic": "",
            "ProductName": "2 year Pickup and Return Notebook Only Service",
            "Brand": "Hewlett Packard Enterprise",
            "BrandID": 13357,
            "ProductRelatedLocales": [
              {
                "ID": 0,
                "Language": "EN",
                "Preferred": 0,
                "StartDate": "",
                "EndDate": ""
              }
            ]
          },
          {
            "ID": 23258676,
            "CategoryID": 152,
            "Preferred": 0,
            "IcecatID": 478323,
            "ProductCode": "EM537ET",
            "ThumbPic": "",
            "ProductName": "3-in-1 NAS Docking Station",
            "Brand": "HP",
            "BrandID": 1,
            "ProductRelatedLocales": [
              {
                "ID": 0,
                "Language": "EN",
                "Preferred": 0,
                "StartDate": "",
                "EndDate": ""
              }
            ]
          },
          {
            "ID": 48885480,
            "CategoryID": 911,
            "Preferred": 0,
            "IcecatID": 465017,
            "ProductCode": "EM995AA",
            "ThumbPic": "",
            "ProductName": "DDR2-667 2GB",
            "Brand": "HP",
            "BrandID": 1,
            "ProductRelatedLocales": [
              {
                "ID": 0,
                "Language": "EN",
                "Preferred": 0,
                "StartDate": "",
                "EndDate": ""
              }
            ]
          },
          {
            "ID": 48885590,
            "CategoryID": 152,
            "Preferred": 0,
            "IcecatID": 464317,
            "ProductCode": "EN488ET",
            "ThumbPic": "",
            "ProductName": "Basic Docking Station with Smart AC Adapter",
            "Brand": "HP",
            "BrandID": 1,
            "ProductRelatedLocales": [
              {
                "ID": 0,
                "Language": "EN",
                "Preferred": 0,
                "StartDate": "",
                "EndDate": ""
              }
            ]
          },
          {
            "ID": 70348957,
            "CategoryID": 911,
            "Preferred": 0,
            "IcecatID": 462528,
            "ProductCode": "EM993ET",
            "ThumbPic": "",
            "ProductName": "512MB DDR2 667MHz",
            "Brand": "HP",
            "BrandID": 1,
            "ProductRelatedLocales": [
              {
                "ID": 0,
                "Language": "EN",
                "Preferred": 0,
                "StartDate": "",
                "EndDate": ""
              }
            ]
          },
          {
            "ID": 22987975,
            "CategoryID": 152,
            "Preferred": 0,
            "IcecatID": 462524,
            "ProductCode": "EN489ET",
            "ThumbPic": "",
            "ProductName": "EN489ET",
            "Brand": "HP",
            "BrandID": 1,
            "ProductRelatedLocales": [
              {
                "ID": 0,
                "Language": "EN",
                "Preferred": 0,
                "StartDate": "",
                "EndDate": ""
              }
            ]
          },
          {
            "ID": 48885575,
            "CategoryID": 911,
            "Preferred": 0,
            "IcecatID": 462512,
            "ProductCode": "EM994ET",
            "ThumbPic": "",
            "ProductName": "DDR2-667 1GB",
            "Brand": "HP",
            "BrandID": 1,
            "ProductRelatedLocales": [
              {
                "ID": 0,
                "Language": "EN",
                "Preferred": 0,
                "StartDate": "",
                "EndDate": ""
              }
            ]
          },
          {
            "ID": 48885565,
            "CategoryID": 1754,
            "Preferred": 0,
            "IcecatID": 462496,
            "ProductCode": "EL347AA",
            "ThumbPic": "",
            "ProductName": "Smart Card Reader with Java Card",
            "Brand": "HP",
            "BrandID": 1,
            "ProductRelatedLocales": [
              {
                "ID": 0,
                "Language": "EN",
                "Preferred": 0,
                "StartDate": "",
                "EndDate": ""
              }
            ]
          },
          {
            "ID": 48885570,
            "CategoryID": 214,
            "Preferred": 0,
            "IcecatID": 460785,
            "ProductCode": "ET353AA",
            "ThumbPic": "",
            "ProductName": "SuperMulti (DL) DVD+/-RW LightScribe Drive",
            "Brand": "HP",
            "BrandID": 1,
            "ProductRelatedLocales": [
              {
                "ID": 0,
                "Language": "EN",
                "Preferred": 0,
                "StartDate": "",
                "EndDate": ""
              }
            ]
          },
          {
            "ID": 48885475,
            "CategoryID": 911,
            "Preferred": 0,
            "IcecatID": 460781,
            "ProductCode": "EM994AA",
            "ThumbPic": "",
            "ProductName": "DDR2-667 1GB",
            "Brand": "HP",
            "BrandID": 1,
            "ProductRelatedLocales": [
              {
                "ID": 0,
                "Language": "EN",
                "Preferred": 0,
                "StartDate": "",
                "EndDate": ""
              }
            ]
          },
          {
            "ID": 147685443,
            "CategoryID": 911,
            "Preferred": 0,
            "IcecatID": 459203,
            "ProductCode": "KTH-ZD8000B/1G",
            "ThumbPic": "",
            "ProductName": "1GB DDR2-667",
            "Brand": "Kingston Technology",
            "BrandID": 18,
            "ProductRelatedLocales": [
              {
                "ID": 0,
                "Language": "EN",
                "Preferred": 0,
                "StartDate": "",
                "EndDate": ""
              }
            ]
          },
          {
            "ID": 21918322,
            "CategoryID": 194,
            "Preferred": 0,
            "IcecatID": 449659,
            "ProductCode": "DT527A#UUZ#*OP",
            "ThumbPic": "",
            "ProductName": "Standard Basic Keyboard 2004 PS2",
            "Brand": "HP",
            "BrandID": 1,
            "ProductRelatedLocales": [
              {
                "ID": 0,
                "Language": "EN",
                "Preferred": 0,
                "StartDate": "",
                "EndDate": ""
              }
            ]
          },
          {
            "ID": 21918321,
            "CategoryID": 194,
            "Preferred": 0,
            "IcecatID": 446654,
            "ProductCode": "DT527A#AC0#*OP",
            "ThumbPic": "",
            "ProductName": "Standard Basic Keyboard 2004 PS2",
            "Brand": "HP",
            "BrandID": 1,
            "ProductRelatedLocales": [
              {
                "ID": 0,
                "Language": "EN",
                "Preferred": 0,
                "StartDate": "",
                "EndDate": ""
              }
            ]
          },
          {
            "ID": 21918320,
            "CategoryID": 194,
            "Preferred": 0,
            "IcecatID": 446621,
            "ProductCode": "DT527A#ABF#*OP",
            "ThumbPic": "",
            "ProductName": "Standard Basic Keyboard 2004 PS2",
            "Brand": "HP",
            "BrandID": 1,
            "ProductRelatedLocales": [
              {
                "ID": 0,
                "Language": "EN",
                "Preferred": 0,
                "StartDate": "",
                "EndDate": ""
              }
            ]
          },
          {
            "ID": 21918319,
            "CategoryID": 194,
            "Preferred": 0,
            "IcecatID": 446560,
            "ProductCode": "DT527A#ABB#*OP",
            "ThumbPic": "",
            "ProductName": "Standard Basic Keyboard 2004 PS2",
            "Brand": "HP",
            "BrandID": 1,
            "ProductRelatedLocales": [
              {
                "ID": 0,
                "Language": "EN",
                "Preferred": 0,
                "StartDate": "",
                "EndDate": ""
              }
            ]
          },
          {
            "ID": 21918318,
            "CategoryID": 194,
            "Preferred": 0,
            "IcecatID": 446483,
            "ProductCode": "DT527A#ABD#*OP",
            "ThumbPic": "",
            "ProductName": "Standard Basic Keyboard 2004 PS2",
            "Brand": "HP",
            "BrandID": 1,
            "ProductRelatedLocales": [
              {
                "ID": 0,
                "Language": "EN",
                "Preferred": 0,
                "StartDate": "",
                "EndDate": ""
              }
            ]
          },
          {
            "ID": 48886000,
            "CategoryID": 152,
            "Preferred": 0,
            "IcecatID": 441071,
            "ProductCode": "PX971A#ABH",
            "ThumbPic": "",
            "ProductName": "Targus Mobile Port Replicator",
            "Brand": "HP",
            "BrandID": 1,
            "ProductRelatedLocales": [
              {
                "ID": 0,
                "Language": "EN",
                "Preferred": 0,
                "StartDate": "",
                "EndDate": ""
              }
            ]
          },
          {
            "ID": 25050978,
            "CategoryID": 1285,
            "Preferred": 0,
            "IcecatID": 377100,
            "ProductCode": "PR277AA",
            "ThumbPic": "",
            "ProductName": "PR277AA",
            "Brand": "HP",
            "BrandID": 1,
            "ProductRelatedLocales": [
              {
                "ID": 0,
                "Language": "EN",
                "Preferred": 0,
                "StartDate": "",
                "EndDate": ""
              }
            ]
          },
          {
            "ID": 25050979,
            "CategoryID": 1285,
            "Preferred": 0,
            "IcecatID": 377087,
            "ProductCode": "PT186AA",
            "ThumbPic": "",
            "ProductName": "PT186AA",
            "Brand": "HP",
            "BrandID": 1,
            "ProductRelatedLocales": [
              {
                "ID": 0,
                "Language": "EN",
                "Preferred": 0,
                "StartDate": "",
                "EndDate": ""
              }
            ]
          },
          {
            "ID": 50470304,
            "CategoryID": 152,
            "Preferred": 0,
            "IcecatID": 360258,
            "ProductCode": "PX971A",
            "ThumbPic": "",
            "ProductName": "PX971A",
            "Brand": "HP",
            "BrandID": 1,
            "ProductRelatedLocales": [
              {
                "ID": 0,
                "Language": "EN",
                "Preferred": 0,
                "StartDate": "",
                "EndDate": ""
              }
            ]
          },
          {
            "ID": 21918317,
            "CategoryID": 194,
            "Preferred": 0,
            "IcecatID": 357973,
            "ProductCode": "DT527A#AKN#*AGFA-HC",
            "ThumbPic": "",
            "ProductName": "Standard Basic Keyboard 2004 PS2",
            "Brand": "HP",
            "BrandID": 1,
            "ProductRelatedLocales": [
              {
                "ID": 0,
                "Language": "EN",
                "Preferred": 0,
                "StartDate": "",
                "EndDate": ""
              }
            ]
          },
          {
            "ID": 50470065,
            "CategoryID": 182,
            "Preferred": 0,
            "IcecatID": 327939,
            "ProductCode": "Q6398A",
            "ThumbPic": "",
            "ProductName": "bt450 Bluetooth Wireless Printer Adapter",
            "Brand": "HP",
            "BrandID": 1,
            "ProductRelatedLocales": [
              {
                "ID": 0,
                "Language": "EN",
                "Preferred": 0,
                "StartDate": "",
                "EndDate": ""
              }
            ]
          },
          {
            "ID": 50470064,
            "CategoryID": 182,
            "Preferred": 0,
            "IcecatID": 322164,
            "ProductCode": "Q6398A#708",
            "ThumbPic": "",
            "ProductName": "bt450 Bluetooth Wireless Printer Adapter",
            "Brand": "HP",
            "BrandID": 1,
            "ProductRelatedLocales": [
              {
                "ID": 0,
                "Language": "EN",
                "Preferred": 0,
                "StartDate": "",
                "EndDate": ""
              }
            ]
          },
          {
            "ID": 22987967,
            "CategoryID": 2509,
            "Preferred": 0,
            "IcecatID": 278412,
            "ProductCode": "PB993ET",
            "ThumbPic": "",
            "ProductName": "PB993ET",
            "Brand": "HP",
            "BrandID": 1,
            "ProductRelatedLocales": [
              {
                "ID": 0,
                "Language": "EN",
                "Preferred": 0,
                "StartDate": "",
                "EndDate": ""
              }
            ]
          },
          {
            "ID": 48885395,
            "CategoryID": 942,
            "Preferred": 0,
            "IcecatID": 265193,
            "ProductCode": "PA507A",
            "ThumbPic": "",
            "ProductName": "Standard Monitor Stand",
            "Brand": "HP",
            "BrandID": 1,
            "ProductRelatedLocales": [
              {
                "ID": 0,
                "Language": "EN",
                "Preferred": 0,
                "StartDate": "",
                "EndDate": ""
              }
            ]
          },
          {
            "ID": 24552070,
            "CategoryID": 2509,
            "Preferred": 0,
            "IcecatID": 265188,
            "ProductCode": "PB993A",
            "ThumbPic": "",
            "ProductName": "PB993A",
            "Brand": "HP",
            "BrandID": 1,
            "ProductRelatedLocales": [
              {
                "ID": 0,
                "Language": "EN",
                "Preferred": 0,
                "StartDate": "",
                "EndDate": ""
              }
            ]
          },
          {
            "ID": 50470043,
            "CategoryID": 2509,
            "Preferred": 0,
            "IcecatID": 265187,
            "ProductCode": "PB994A",
            "ThumbPic": "",
            "ProductName": "6-cell 55Wh Li-Ion Primary Battery",
            "Brand": "HP",
            "BrandID": 1,
            "ProductRelatedLocales": [
              {
                "ID": 0,
                "Language": "EN",
                "Preferred": 0,
                "StartDate": "",
                "EndDate": ""
              }
            ]
          },
          {
            "ID": 48885425,
            "CategoryID": 214,
            "Preferred": 0,
            "IcecatID": 265165,
            "ProductCode": "PA851A",
            "ThumbPic": "",
            "ProductName": "External MultiBay II SuperMulti (DL) DVD+/-RW Drive",
            "Brand": "HP",
            "BrandID": 1,
            "ProductRelatedLocales": [
              {
                "ID": 0,
                "Language": "EN",
                "Preferred": 0,
                "StartDate": "",
                "EndDate": ""
              }
            ]
          },
          {
            "ID": 48885145,
            "CategoryID": 869,
            "Preferred": 0,
            "IcecatID": 149455,
            "ProductCode": "DC851B#ABH",
            "ThumbPic": "",
            "ProductName": "DC851B",
            "Brand": "HP",
            "BrandID": 1,
            "ProductRelatedLocales": [
              {
                "ID": 0,
                "Language": "EN",
                "Preferred": 0,
                "StartDate": "",
                "EndDate": ""
              }
            ]
          },
          {
            "ID": 48885370,
            "CategoryID": 977,
            "Preferred": 0,
            "IcecatID": 130249,
            "ProductCode": "PC766A",
            "ThumbPic": "",
            "ProductName": "Kensington MicroSaver",
            "Brand": "HP",
            "BrandID": 1,
            "ProductRelatedLocales": [
              {
                "ID": 0,
                "Language": "EN",
                "Preferred": 0,
                "StartDate": "",
                "EndDate": ""
              }
            ]
          },
          {
            "ID": 48885365,
            "CategoryID": 211,
            "Preferred": 0,
            "IcecatID": 107341,
            "ProductCode": "DC361B",
            "ThumbPic": "",
            "ProductName": "USB External Diskette Drive",
            "Brand": "HP",
            "BrandID": 1,
            "ProductRelatedLocales": [
              {
                "ID": 0,
                "Language": "EN",
                "Preferred": 0,
                "StartDate": "",
                "EndDate": ""
              }
            ]
          },
          {
            "ID": 48885186,
            "CategoryID": 194,
            "Preferred": 0,
            "IcecatID": 102875,
            "ProductCode": "DT527A#ABH",
            "ThumbPic": "",
            "ProductName": "PS/2 Standard Keyboard",
            "Brand": "HP",
            "BrandID": 1,
            "ProductRelatedLocales": [
              {
                "ID": 0,
                "Language": "EN",
                "Preferred": 0,
                "StartDate": "",
                "EndDate": ""
              }
            ]
          },
          {
            "ID": 133905566,
            "CategoryID": 194,
            "Preferred": 0,
            "IcecatID": 95950,
            "ProductCode": "DT528A#ABH",
            "ThumbPic": "",
            "ProductName": "USB Standard Keyboard",
            "Brand": "HP",
            "BrandID": 1,
            "ProductRelatedLocales": [
              {
                "ID": 0,
                "Language": "EN",
                "Preferred": 0,
                "StartDate": "",
                "EndDate": ""
              }
            ]
          },
          {
            "ID": 48885144,
            "CategoryID": 869,
            "Preferred": 0,
            "IcecatID": 49181,
            "ProductCode": "DC851B",
            "ThumbPic": "",
            "ProductName": "DC851B",
            "Brand": "HP",
            "BrandID": 1,
            "ProductRelatedLocales": [
              {
                "ID": 0,
                "Language": "EN",
                "Preferred": 0,
                "StartDate": "",
                "EndDate": ""
              }
            ]
          }
        ],
        "Variants": [
          {
            "VariantID": "203337",
            "VariantIdentifiers": [
              {
                "Identifier Type": "GTIN13",
                "Value": "0884420156116"
              },
              {
                "Identifier Type": "BrandProductCode",
                "Value": "KE125ET#ABD"
              }
            ],
            "VariantFeatures": [],
            "VariantImages": [],
            "VariantMultimedia": [],
            "VariantDescriptions": "C6710bUT8300W5X16GIBH20Qa GR - Germany - German localization"
          },
          {
            "VariantID": "203339",
            "VariantIdentifiers": [
              {
                "Identifier Type": "GTIN13",
                "Value": "0883585922451"
              },
              {
                "Identifier Type": "BrandProductCode",
                "Value": "KE125ET#UUZ"
              }
            ],
            "VariantFeatures": [],
            "VariantImages": [],
            "VariantMultimedia": [],
            "VariantDescriptions": "C6710bUT8300W5X16GIBH20Qa SWIS2 - Switzerland-German/French/Ital"
          },
          {
            "VariantID": "203340",
            "VariantIdentifiers": [
              {
                "Identifier Type": "GTIN13",
                "Value": "0883585927562"
              },
              {
                "Identifier Type": "BrandProductCode",
                "Value": "KE125ET#ABN"
              }
            ],
            "VariantFeatures": [],
            "VariantImages": [],
            "VariantMultimedia": [],
            "VariantDescriptions": "C6710bUT8300W5X16GIBH20Qa NOR - Norway - Norwegian localizatio"
          },
          {
            "VariantID": "203344",
            "VariantIdentifiers": [
              {
                "Identifier Type": "GTIN13",
                "Value": "0884420151241"
              },
              {
                "Identifier Type": "BrandProductCode",
                "Value": "KE125ET#ABU"
              }
            ],
            "VariantFeatures": [],
            "VariantImages": [],
            "VariantMultimedia": [],
            "VariantDescriptions": "C6710bUT8300W5X16GIBH20Qa UK - United Kingdom - UK English lo"
          },
          {
            "VariantID": "203345",
            "VariantIdentifiers": [
              {
                "Identifier Type": "GTIN13",
                "Value": "0883585931712"
              },
              {
                "Identifier Type": "BrandProductCode",
                "Value": "KE125ET#AK8"
              }
            ],
            "VariantFeatures": [],
            "VariantImages": [],
            "VariantMultimedia": [],
            "VariantDescriptions": "C6710bUT8300W5X16GIBH20Qa SE/FI - Sweden/Finland - se/fi/en loca"
          },
          {
            "VariantID": "519235",
            "VariantIdentifiers": [
              {
                "Identifier Type": "GTIN13",
                "Value": "0883585922710"
              },
              {
                "Identifier Type": "BrandProductCode",
                "Value": "KE125ET#UUG"
              }
            ],
            "VariantFeatures": [],
            "VariantImages": [],
            "VariantMultimedia": [],
            "VariantDescriptions": "C6710bUT8300W5X16GIBH20Qa EUROA4 - Belgium - en/nl/fr/de localiza"
          }
        ],
        "ProductStory": [],
        "DemoAccount": false
      }
    }]
    """
