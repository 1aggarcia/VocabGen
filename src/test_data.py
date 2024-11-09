"""
HTML page to test parsing

Source: https://www.wordreference.com/esit/nevar
"""

EXAMPLE_PAGE = """
<!DOCTYPE html>
<html class="desktop osx" lang="en" translate="no">
<head>
    <link rel="preload" as="script" type="text/javascript" href="https://www.wordreference.com/js/prebid_latest.js">
<link rel="preload" as="script" type="text/javascript" href="https://c.amazon-adsystem.com/aax2/apstag.js">
<link rel="preload" as="script" type="text/javascript" href="https://c.amazon-adsystem.com/bao-csm/aps-comm/aps_csm.js">
<link rel="preload" as="script" type="text/javascript" href="https://securepubads.g.doubleclick.net/tag/js/gpt.js">

<link rel="dns-prefetch" href="//cdn77w.wordreference.net">
<link rel="dns-prefetch" href="//www.google-analytics.com">

<link rel="preconnect" href="https://ad.doubleclick.net">
<link rel="preconnect" href="https://ib.adnxs.com">
<link rel="preconnect" href="https://acdn.adnxs.com">
<link rel="preconnect" href="https://ssum-sec.casalemedia.com">
<link rel="preconnect" href="https://onetag-sys.com">
<link rel="preconnect" href="https://u.openx.net">
<link rel="preconnect" href="https://fastlane.rubiconproject.com">
<link rel="preconnect" href="https://eus.rubiconproject.com">
<link rel="preconnect" href="https://contextual.media.net">
<link rel="preconnect" href="https://hbopenbid.pubmatic.com">
<link rel="preconnect" href="https://ads.pubmatic.com">
<link rel="preconnect" href="https://ap.lijit.com">
<link rel="preconnect" href="https://aax-eu.amazon-adsystem.com">
    
<meta http-equiv="Content-type" content="text/html;charset=UTF-8">
<title>nevar - WordReference.com Dictionary of English</title>
<meta name="description" content="nevar - WordReference English dictionary, questions, discussion and forums. All Free.">
<meta http-equiv="Content-Language" content="en">
<link title="WR definition" rel="search" type="application/opensearchdescription+xml" href="https://www.wordreference.com/home/OpenSearch?dict=esit">

<!-- Don't index virtual dictionaries -->
<META NAME='ROBOTS' CONTENT='NOINDEX,NOFOLLOW'>
<meta name="robots" content="notranslate">
<meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=4, minimum-scale=0.1, user-scalable=yes">
<meta property="og:image" content="//www.wordreference.com/images/WR_fbicon_200x200.png" />
<meta name="webkey" content="7i+MFsJWdPNgdRY9vleCzUsZtlGj/rAf6AbybxOsV8Q=">




<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-WV46ZWEMKW"></script>
<script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){dataLayer.push(arguments);}
    gtag('js', new Date());

    gtag('config', 'G-WV46ZWEMKW');

        
    gtag('set', {'dimension5': 'US'});
</script>
<script>
    window.onerror = function(message, file, line) { 
        var sFormattedMessage = new Date().toLocaleString() + ' - [' + file + ' (' + line + ')][' + window.navigator.userAgent + '] ' + message; 
        sFormattedMessage = sFormattedMessage.length > 150 ? sFormattedMessage.substring(0, 150) : sFormattedMessage;
        gtag('event', 'exception', {
            'description': sFormattedMessage,
            'fatal': false
        });
    }
</script>

<script>
    //#1376: This function write messages to the browser's console but it checked first if they are allowed

            var consoleDebug = function(){};
        

            //This will send an event to GA
            var sendGAEvent = sendGAEvent || function (category, action, label, value, callback){
                gtag('event', action, {
                    'event_category': category,
                    'event_label': label,
                    'value': value,
                    'non_interaction': true,
                    'event_callback': function() {
                            callback();
                        }
                });
            };
        

            var googletag = googletag || {};
            googletag.cmd = googletag.cmd || [];
        </script>




    

        <script>
            var googletag = googletag || {};
            googletag.cmd = googletag.cmd || [];
        </script>
        <script async data-cfasync="false" src="https://cdn.snigelweb.com/adengine/wordreference.com/loader.js" type="text/javascript"></script>
        
          <script>

            //This will send an event to GA
            function sendGAEvent(category, action, label, value, callback){
                gtag('event', action, {
                    'event_category': category,
                    'event_label': label,
                    'value': value,
                    'non_interaction': true,
                    'event_callback': function() {
                            callback();
                        }
                });
            }

            var consentReady = false;
            var consentExec = function() {
                window.wrconsent = window.wrconsent || {};
                window.wrconsent.gdpr = window.wrconsent.gdpr || {};
                window.wrconsent.ccpa = window.wrconsent.ccpa || {};

                //Set personalized ads value 
                //More here: https://developers.google.com/publisher-tag/reference#googletag.privacysettingsconfig
                function setPersonalizedAds(value){
                  var googletag = googletag || {};
                  googletag.cmd = googletag.cmd || [];
                  googletag.cmd.push(function() {
                      // Set privacy settings for CCPA compliance
                      // No need to use 'nonPersonalizedAds', it will be redundant since we already have CMP implemented
                      googletag.pubads().setPrivacySettings({
                        'restrictDataProcessing': !value,       //to comply with CCPA regulations, ensuring that personal data is not used for personalized advertising or other purposes that involve data processing
                      });

                      // Set request for non-personalized ads (0 for personalized, 1 for non-personalized)
                      googletag.pubads().setRequestNonPersonalizedAds(!value ? 1 : 0);
                  });
                }   

                // Make sure that the properties exist on the window.
                window.googlefc = window.googlefc || {};
                window.googlefc.ccpa = window.googlefc.ccpa || {}
                window.googlefc.callbackQueue = window.googlefc.callbackQueue || [];

            
                //Get the user consent            
                var consents = {};
                var legitimateInterests = {};
                var personalizedAdsAccepted = false, nonPersonalizedAdsAccepted = false, limitedAdsAccepted = false;
                //setPersonalizedAds(false);    //Useless in TCF v2: GPT will gather the consent string automatically

                //Set the user consent
                const checkGDPRConsent = (tcData, success) => {   
                  consoleDebug("*** GDPR applies");           
                  consoleDebug('++* tcData', tcData, success);
                  if(success && tcData.gdprApplies &&
                    (tcData.eventStatus === 'useractioncomplete' || tcData.eventStatus === 'tcloaded')) {
                    window.wrconsent.gdpr.gdprApplies = true;
                    // do something with tcData.tcString
                    consents = tcData.purpose.consents;
                    legitimateInterests = tcData.purpose.legitimateInterests;
                    consoleDebug('++ consents', consents);

                    //Set the personalized ads for DFP
                    // More: https://support.google.com/admanager/answer/9805023
                    personalizedAdsAccepted = consents[1] && consents[3] && consents[4]
                                              && ((legitimateInterests[2] || consents[2]) && 
                                                  (legitimateInterests[7] || consents[7]) && 
                                                  (legitimateInterests[9] || consents[9]) && 
                                                  (legitimateInterests[10] || consents[10]));
                    nonPersonalizedAdsAccepted = consents[1]
                                                 && ((legitimateInterests[2] || consents[2]) && 
                                                     (legitimateInterests[7] || consents[7]) && 
                                                     (legitimateInterests[9] || consents[9]) && 
                                                     (legitimateInterests[10] || consents[10]));
                    limitedAdsAccepted = !consents[1] 
                                         && ((legitimateInterests[2] || consents[2]) && 
                                             (legitimateInterests[7] || consents[7]) && 
                                             (legitimateInterests[9] || consents[9]) && 
                                             (legitimateInterests[10] || consents[10]));

                    //Update Google Consent Mode

                    if(personalizedAdsAccepted){
                      consoleDebug('++ Personalized ads accepted by the user.');
                    } else if (nonPersonalizedAdsAccepted){
                      consoleDebug('++ Non personalized ads accepted by the user.');
                    } else if (limitedAdsAccepted) {
                      //consoleDebug('++ Limited ads accepted by the user.');
                    } else {
                      consoleDebug('++ Ads are not accepted by the user.');
                    }

                    consentReady = true;    //Ad requests can start
                    consoleDebug('++* Call startAuction from GDPR section.');
                    googletag.cmd.push(function(){
	                    pbjs.que.push(function() {
                            startAuction();         //Start the auction
                    	});
                    });
                    window.wrconsent.auctionStarted = true;

                    //These variables are used for stats
                    var GDPRnoCookie = true;
                    var GDPRconsent = personalizedAdsAccepted;
                    var GDPRnoConsent = !personalizedAdsAccepted;
                    var GDPRconsentAllAccepted = consents[1] && consents[2] && consents[3] && consents[4] && consents[5] && consents[6] && consents[7] && consents[8] && consents[9] && consents[10];
                    var GDPRconsentAllRejected = !consents[1] && !consents[2] && !consents[3] && !consents[4] && !consents[5] && !consents[6] && !consents[7] && !consents[8] && !consents[9] && !consents[10];
                
                    //Report the euconsent cookie state (only for EU users)
                    if(GDPRconsent)
                        sendGAEvent('GDPR', 'GDPR-consent', 'GDPR-consent-' + GDPRconsent, (GDPRconsent ? '1' : '0'), function() { consoleDebug(":> GDPR: GDPR-consent-"  + GDPRconsent + " -> GA"); });
                    if(GDPRnoConsent)
                        sendGAEvent('GDPR', 'GDPR-noConsent', 'GDPR-noConsent-' + GDPRnoConsent, (GDPRnoConsent ? '1' : '0'), function() { consoleDebug(":> GDPR: GDPR-noConsent-"  + GDPRnoConsent + " -> GA"); });
                    if(GDPRnoCookie)
                        sendGAEvent('GDPR', 'GDPR-noCookie', 'GDPR-noCookie-' + GDPRnoCookie, (GDPRnoCookie ? '1' : '0'), function() { consoleDebug(":> GDPR: GDPR-noCookie-"  + GDPRnoCookie + " -> GA"); });
                    if(GDPRconsentAllAccepted)
                        sendGAEvent('GDPR', 'GDPR-consentAllAccepted', 'GDPR-consentAllAccepted-' + GDPRconsentAllAccepted, (GDPRconsentAllAccepted ? '1' : '0'), function() { consoleDebug(":> GDPR: GDPR-consentAllAccepted-"  + GDPRconsentAllAccepted + " -> GA"); });
                    if(GDPRconsentAllRejected)
                        sendGAEvent('GDPR', 'GDPR-consentAllRejected', 'GDPR-consentAllRejected-' + GDPRconsentAllRejected, (GDPRconsentAllRejected ? '1' : '0'), function() { consoleDebug(":> GDPR: GDPR-consentAllRejected-"  + GDPRconsentAllRejected + " -> GA"); });

                    // remove the event handler to not get called more than once
                    __tcfapi('removeEventListener', 2.2, (success) => {
                      if(success) {
                        // oh good...
                        consoleDebug('++ CMP listener removed.');
                      }
                    }, tcData.listenerId);

                    //If the user did not accept at least purpose 1 and Google, ads won't show up
                    var isGoogleConsented = (tcData.vendor.consents[755] && tcData.vendor.legitimateInterests[755]) || false;
                    var isPurposeOneConsented = consents[1] || false;
                    consoleDebug('** isPurposeOneConsented:', isPurposeOneConsented);
                    consoleDebug('** isGoogleConsented:', isGoogleConsented);

                    //Fill wrconsent.gdpr and decide weather ads are consented or not
                    window.wrconsent.gdpr.consents = consents;
                    window.wrconsent.gdpr.legitimateInterests = legitimateInterests;
                    window.wrconsent.gdpr.isGoogleVendorConsented = isGoogleConsented;
                    window.wrconsent.gdpr.isPurposeOneConsented = isPurposeOneConsented;
                    window.wrconsent.gdpr.personalizedAdsAccepted = personalizedAdsAccepted;
                    window.wrconsent.gdpr.nonPersonalizedAdsAccepted = nonPersonalizedAdsAccepted;
                    window.wrconsent.gdpr.limitedAdsAccepted = limitedAdsAccepted;
                    window.wrconsent.gdpr.adsAllowed = (!window.wrconsent.gdpr.gdprApplies || 
                                                       (isGoogleConsented && personalizedAdsAccepted) || 
                                                       //(limitedAdsAccepted) || 
                                                       (isGoogleConsented && nonPersonalizedAdsAccepted));
                    window.wrconsent.isPremiumUser = false;

                    //Save consent status
                    saveWRConsentStatus();
                  }
                  else if (success && !tcData.gdprApplies){
                      window.wrconsent.gdpr.gdprApplies = false;
                      consoleDebug('++ GDPR does not apply.');
                      noConsentNeeded();
                  }
                }            

                const checkUSPConsent = (uspData, success) => { 
                  //consoleDebug("*** CCPA applies");
                  consoleDebug('++* uspData', uspData);
              
                  //uspConsent parsing
                  var CCPAArray = uspData.uspString.split("");
                  var CCPAApplies = (uspData.uspString !== "1---");
                  var CCPANotice = (CCPAArray[1] === 'Y');
                  var CCPAOptOut = (CCPAArray[2] === 'Y');

                  setPersonalizedAds(!CCPAOptOut);
                  if(CCPAOptOut)
                    consoleDebug('++* Don\'t show personalized ads.');
                  else
                    consoleDebug('++* Show personalized ads.');
              
                  //Report the CCPA consent state (only for US CA users)
                  if(CCPAApplies){
                      sendGAEvent('CCPA', 'CCPA-applicable', 'CCPA-applicable-' + CCPAApplies, (CCPAApplies ? '1' : '0'), function() { consoleDebug(":> CCPA: CCPA-applicable-"  + CCPAApplies + " -> GA"); });
                      sendGAEvent('CCPA', 'CCPA-notice', 'CCPA-notice-' + CCPANotice, (CCPANotice ? '1' : '0'), function() { consoleDebug(":> CCPA: CCPA-Notice-"  + CCPANotice + " -> GA"); });
                      sendGAEvent('CCPA', 'CCPA-OptOut', 'CCPA-OptOut-' + CCPAOptOut, (CCPAOptOut ? '1' : '0'), function() { consoleDebug(":> CCPA: CCPA-OptOut-"  + CCPAOptOut + " -> GA"); });
                  }

                  consentReady = true;    //Ad requests can start
                  consoleDebug('++* Call startAuction from USP section.');
                  googletag.cmd.push(function(){
	                    pbjs.que.push(function() {
                            startAuction();         //Start the auction
                  	    });
                  });
                  window.wrconsent.auctionStarted = true;
                }

                const noConsentNeeded = () => { 
                    //Both ccpa and gdpr should be checked first
                    consoleDebug('++* No consent is needed');
                    if(window.wrconsent.gdprApplies || window.wrconsent.ccpaApplies){      //Set personalized ads in the case of ccpa only
                        consoleDebug('++* Something wrong happened. Don\'t show personalized ads.');
                        if(!window.wrconsent.gdprApplies) {       //In GDPR case, personalized ads is set automatically through TCF
                            consoleDebug('++* Don\'t show personalized ads.');
                            setPersonalizedAds(false);
                        }
                    } else {
                        consoleDebug('++* Show personalized ads.');
                        setPersonalizedAds(true);
                    }
                    consoleDebug('++* Call startAuction from noConsentNeeded');
                    consentReady = true;    //Ad request can start                        
                    googletag.cmd.push(function(){
	                    pbjs.que.push(function() {
                            startAuction();         //Start the auction
                    	});
                    });
                    window.wrconsent.auctionStarted = true;
                }            

                // Queue the callback on the callbackQueue.

                    googlefc.callbackQueue.push({
                        'INITIAL_CCPA_DATA_READY':
                        () => {
                            switch (googlefc.ccpa.getInitialCcpaStatus()) {
                                case googlefc.ccpa.InitialCcpaStatusEnum.UNKNOWN:
                                    // Something failed, in an unknown state.
                                    consoleDebug('++* CCPA something wrong happened.');
                                    window.wrconsent.ccpa.ccpaApplies = false;
                                    window.wrconsent.ccpa.uspString = "1---";
                                    consoleDebug('++* CCPA does not apply.');
                                    noConsentNeeded();
                                    break;
                                case googlefc.ccpa.InitialCcpaStatusEnum.CCPA_DOES_NOT_APPLY:
                                    // Insert handling for cases where the user is not CCPA eligible.
                                    window.wrconsent.ccpa.ccpaApplies = false;
                                    window.wrconsent.ccpa.uspString = "1---";
                                    consoleDebug('++* CCPA does not apply.');
                                    noConsentNeeded();
                                    break;
                                case googlefc.ccpa.InitialCcpaStatusEnum.NOT_OPTED_OUT:
                                    // Insert handling for cases where the user is CCPA eligible and has
                                    // not opted out.
                                    window.wrconsent.ccpa.ccpaApplies = true;
                                    window.wrconsent.ccpa.optedOut = false;
                                    consoleDebug('++* CCPA not opted out.');
                                    __uspapi('getUSPData', 1 , (uspData, success) => {
                                        if(success) {
                                            window.wrconsent.ccpa.uspString = uspData.uspString;
                                            checkUSPConsent(uspData, success);
                                        } else {
                                            //Something wrong happened, try to start the auction with personalized ads set to false
                                            window.wrconsent.ccpa.uspString = "1NNN";
                                            noConsentNeeded();
                                        }
                                    });
                                    break;
                                case googlefc.ccpa.InitialCcpaStatusEnum.OPTED_OUT:
                                    // Insert handling for cases where the user is CCPA eligible and has
                                    // opted out.
                                    window.wrconsent.ccpa.ccpaApplies = true;
                                    window.wrconsent.ccpa.optedOut = true;
                                    consoleDebug('++* CCPA opted out.');
                                    __uspapi('getUSPData', 1 , (uspData, success) => {
                                        if(success) {
                                            checkUSPConsent(uspData, success);
                                            window.wrconsent.ccpa.uspString = uspData.uspString;
                                        } else {
                                            //Something wrong happened, try to start the auction
                                            window.wrconsent.ccpa.uspString = "1NYN";
                                            noConsentNeeded();
                                        }
                                    });
                                    break;
                            }
                        }
                    });
                    window.wrconsent.gdpr.gdprApplies = false;
                                }

            //If inside an iframe, don't check the consent and don't run the Auction (no ads)
            document.addEventListener("DOMContentLoaded", function(event) {
                //Use a timer to reduce the Total Blocking Time (web vitals)
                if (!inIframe())
                    consentExec(); //Show the Ads
            });   
                    </script>

        <script>
            gtag('event', 'Snigel-Inserted', {
                'event_category': 'Snigel',
                'event_label': 'Snigel-Inserted',
                'value': '1',
                'non_interaction': true,
                'event_callback': function() {
                        consoleDebug(":> Snigel: Snigel-Inserted" + " -> GA");
                    }
            });
        </script>

    







    <style type="text/css">
        :root{--main-color:#5e58c7;--red-color:#f00;--bg-color:#fff;--body-text-color:#222;--body-highlighted-text-color:#039;--sentences-color:rgba(0,0,0,.65);--link-color:#0645ad;--visited-link-color:#819;--bold-color:#039;--gray-color:#707070;--highlight-color:#f2f2f7;--row-color:#dcdcdc;--tag-border-color:#c5c5c5;--border-color:#dcdcdc;--search-input-border-color:var(--border-color);--search-btn-border-color:var(--border-color);--warnnote-main-border-color:#e5e4e4;--warnnote-border-color:#ccc;--wotd-border-color:#bdbdbd;--wotd-border-top-color:#3a3498;--close-icon-stroke:#fff;--close-icon-circle-stroke:#c8c8c8;--content-bg-color:#f9f9f9;--ad-bg-color:#f9f9f9;--header-tabs-bg-color:#f9f9fa;--wotd-subscribe-bg-color:#f0f0f0;--search-bg-color:#ebebf2;--search-btn-bg-color:#d7d7d7;--warnnote-bg-color:#f4f4f4;--dict-translation-hover-bg-color:#dfdfdf;--heavy-user-bg-color:#ffffc8;--wotd-bg-color:#fff;--ad-placeholder-bg:#353535;--placeholder-color:#b3b3b3;--placeholder-focus-color:#fff;--term-copy-color:#f66;--try-me-msg-color:#666;--more-pron-trigger-color:#666;--dark-mode-icon-path-fill-color:#666;--dark-mode-icon-path-fill-first-time-color:#b90701;--header-text-color:#f8f7ff;--header-link-color:#f8f7ff;--header-link-span-color:#b2aef4;--header-link-h1-color:#e5e3ff;--header-hover-color:#ddf;--select-bg-color:var(--search-btn-bg-color);--select-border-color:var(--border-color);--select-option-bg-color:var(--search-btn-bg-color);--custom-select-focus-box-shadow:#ccc;--wotd-subscribe-btn-bg-color:#5e58c6;--wotd-subscribe-btn-hover-bg-color:transparent;--wotd-subscribe-btn-hover-color:#5e58c6;--wotd-box-shadow-color:#00000042;--wotd-term-hover-color:#666;--rowhighlight-color:#ffd700;--audio-controls-hover-color:#000;--heavy-user-hover-border-color:#6f6e6e;--selected-term-arrow-color:#000;--warnnote-icon-color:#000;--box-shadow-color:rgba(0,0,0,.12);--loader-border-top-color:rgba(0,0,0,.2);--input-placeholder-color:rgba(0,5,143,.4);--header-tabs-selected-border-color:var(--body-text-color);--sticky-search-box-shadow:#00000075;--copy-ctmenu-border:#000;--copy-ctmenu-label-color:#000;--left-col-title1-color:#777;--explanatory-border-color:#e9e4da;--explanatory-background-color:#fffaf0;--modal-background-color:rgba(0,0,0,.4);--modal-fallback-background-color:#000;--modal-content-background-color:#fefefe;--modal-border-color:#888;--modal-box-shadow-color:rgba(0,0,0,.26);--close-button-color:#aaa;--close-button-hover-focus-color:#000;--key-background-color:#000;--key-color:#ccc;--code-background-color:#dddcdc;--code-color:#000;--announcement-text-color:var(--body-text-color);--announcement-border-color:#dcdce6;--announcement-background-color:#f2f2f7;--announcement-important-text-color:var(--body-text-color);--announcement-important-border-color:#000;--announcement-important-background-color:#fadb4e;--BOXW_warning-color:#fff;--BOXW_warning-bg-color:#999;--strk-st-color1:red;--strk-st-color2:red;--button-border-color:var(--border-color);--button-bg-color:#d7d7d7;--button-hover-border-color:#afaeae;--button-hover-bg-color:#dedede;--swiper-spinner-border-color:rgba(0,0,0,.1);--swiper-spinner-border-left-color:#09f;--swiper-error-color:#f00;--swiper-pagination-bullet-background:#000;--swiper-pagination-bullet-hover-background:#5e58c7;--swiper-header-tabs-background-color:#f8f8f8;--swiper-header-tabs-border-bottom-color:#ddd;--swiper-header-tabs-color:#555;--swiper-header-tabs-hover-background-color:#eee;--swiper-header-tabs-selected-color:#7068f2;--swiper-header-tabs-selected-hover-color:#7068f2;--swiper-header-tabs-selected-border-bottom-color:var(--main-color);--swiper-scrollbar-thumb-background:#ccc;--swiper-scrollbar-thumb-hover-background:#aaa;--swiper-scrollbar-track-background:#f8f8f8;--conj-header-bg-color:#e0e0e8;--conj-temp-header-bg-color:#bcbcbc;--conj-pron-header-bg-color:#e0e0e8;--conj-body-highlighted-text-color:#66f;--conj-link-color:var(--link-color);--conj-visited-link-color:var(--visited-link-color);--index-link-color:#a0a0a0;--index-link-hover-color:#555;--index-section-header-bg-color:#ebebf2;--index-section-header-text-color:#124b94;--index-section-bg-color:#f6f6f8;--index-section-text-color:#9d9d9d;--index-section-border-color:#ccc;--index-section-separator-color:#ccc;--index-control-special-bg-color:inherit;--index-navbar-text-color:#eee;--index-navbar-bg-color:var(--main-color);--index-navbar-link-hover-color:#fff;--index-navbar-menu-bg-color:#fff;--index-navbar-menu-element-bg-color:#fff;--index-navbar-menu-separator-color:#eee;--index-navbar-link-color:#555;--index-navbar-menu-element-hover-color:#eee;--index-navbar-submenu-link-hover:#124b94;--index-footer-menu-header-color:#124b94;--index-footer-menu-border-top-color:rgba(255,255,255,.1);--index-footer-menu-border-bottom-color:rgba(0,0,0,.3);--index-footer-menu-element-color:#124b94;--index-footer-menu-bg-color:#fff;--index-footer-menu-separator-color:rgba(0,0,0,.1);--virt-footer-bg-color:var(--index-navbar-bg-color);--virt-table-border-color:var(--gray-color);--virt-table-text-color:#727272;--virt-table-hover-bg-color:var(--rowhighlight-color);--virt-table-same-color:var(--row-color);--virt-highlight-color:var(--highlight-color);--virt-link-color:var(--link-color);--virt-link-hover-color:var(--index-link-hover-color)}.dark-mode{--main-color:#5e58c7;--red-color:#f66;--bg-color:#121212;--body-text-color:#ddd;--body-highlighted-text-color:#6e66ff;--sentences-color:#ddd;--link-color:#a0a0a0;--visited-link-color:#888;--bold-color:#bbb;--gray-color:#c1c1c1;--highlight-color:#2a2a2a;--row-color:#555;--tag-border-color:#444;--border-color:#555;--search-input-border-color:var(--border-color);--search-btn-border-color:var(--border-color);--warnnote-main-border-color:#444;--warnnote-border-color:#555;--wotd-border-color:#444;--wotd-border-top-color:#3a3498;--close-icon-stroke:#ddd;--close-icon-circle-stroke:#555;--content-bg-color:#1e1e1e;--ad-bg-color:#333;--header-tabs-bg-color:#444;--wotd-subscribe-bg-color:#1e1e1e;--search-bg-color:#2f2f33;--search-btn-bg-color:#333;--warnnote-bg-color:#1e1e1e;--dict-translation-hover-bg-color:#2f2f33;--heavy-user-bg-color:#222;--wotd-bg-color:#1e1e1e;--ad-placeholder-bg:#353535;--placeholder-color:#b3b3b3;--placeholder-focus-color:#fff;--term-copy-color:#f66;--try-me-msg-color:#666;--more-pron-trigger-color:#666;--dark-mode-icon-path-fill-color:#ddd;--dark-mode-icon-path-fill-first-time-color:#b90701;--header-text-color:#ddd;--header-link-color:#ccc;--header-link-span-color:#bbb;--header-link-h1-color:#ddd;--header-hover-color:#4d4d53;--select-bg-color:var(--search-btn-bg-color);--select-border-color:var(--border-color);--select-option-bg-color:var(--search-btn-bg-color);--custom-select-focus-box-shadow:#555;--wotd-subscribe-btn-bg-color:#5e58c6;--wotd-subscribe-btn-hover-bg-color:transparent;--wotd-subscribe-btn-hover-color:#5e58c6;--wotd-box-shadow-color:#00000042;--wotd-term-hover-color:#ddd;--rowhighlight-color:#4f470f;--audio-controls-hover-color:#ddd;--heavy-user-hover-border-color:#6f6e6e;--selected-term-arrow-color:#ddd;--warnnote-icon-color:#ddd;--box-shadow-color:rgba(0,0,0,.12);--loader-border-top-color:rgba(0,0,0,.2);--input-placeholder-color:#adadad66;--header-tabs-selected-border-color:var(--body-text-color);--sticky-search-box-shadow:#00000075;--copy-ctmenu-border:#555;--copy-ctmenu-label-color:#ccc;--left-col-title1-color:#c1c1c1;--ac-text-color:var(--body-text-color);--ac-bg-color:var(--select-bg-color);--ac-border-color:var(--select-border-color);--ac-separator-color:var(--border-color);--modal-content-background-color:var(--bg-color);--modal-border-color:var(--border-color);--close-button-color:#aaa;--close-button-hover-focus-color:#464646;--explanatory-border-color:var(--border-color);--explanatory-background-color:var(--highlight-color);--key-background-color:#ccc;--key-color:#000;--announcement-text-color:var(--body-text-color);--announcement-border-color:#747272;--announcement-background-color:var(--highlight-color);--announcement-important-text-color:#2f2f33;--announcement-important-border-color:#a57615;--announcement-important-background-color:#ab9532;--BOXW_warning-color:var(--body-text-color);--BOXW_warning-bg-color:#555;--strk-st-color1:#f2f2f7;--strk-st-color2:#707070;--button-border-color:var(--border-color);--button-bg-color:#333;--button-hover-border-color:#3d3d3d;--button-hover-bg-color:#4a4949;--swiper-spinner-border-color:rgba(0,0,0,.1);--swiper-spinner-border-left-color:var(--header-tabs-color);--swiper-error-color:#f00;--swiper-pagination-bullet-background:var(--header-tabs-selected-hover-color);--swiper-pagination-bullet-hover-background:#fff;--swiper-header-tabs-background-color:var(--body-bg-color1);--swiper-header-tabs-border-bottom-color:#65656d;--swiper-header-tabs-color:#a1a1ae;--swiper-header-tabs-hover-background-color:#4d4d53;--swiper-header-tabs-selected-color:#7068f2;--swiper-header-tabs-selected-hover-color:#d2cfff;--swiper-header-tabs-selected-border-bottom-color:var(--main-color);--swiper-scrollbar-thumb-background:#ccc;--swiper-scrollbar-thumb-hover-background:#aaa;--swiper-scrollbar-track-background:#f8f8f8;--conj-header-bg-color:#2a2a2a;--conj-temp-header-bg-color:#2a2a2a;--conj-pron-header-bg-color:#2a2a2a;--conj-body-highlighted-text-color:#66f;--conj-link-color:#6e66ff;--conj-visited-link-color:#9e65fa;--index-link-color:#a0a0a0;--index-link-hover-color:#555;--index-section-header-bg-color:#333;--index-section-header-text-color:#ddd;--index-section-bg-color:#1e1e1e;--index-section-text-color:#ccc;--index-section-border-color:#444;--index-section-separator-color:#555;--index-control-special-bg-color:var(--control-bg-color);--index-navbar-text-color:var(--body-text-color);--index-navbar-bg-color:#333;--index-navbar-link-color:#ccc;--index-navbar-link-hover-color:#ccc;--index-navbar-menu-bg-color:#444;--index-navbar-menu-element-hover-color:#555;--index-navbar-menu-element-bg-color:#222;--index-navbar-menu-separator-color:#000;--index-navbar-submenu-link-hover:#124b94;--index-footer-menu-header-color:#124b94;--index-footer-menu-border-top-color:rgba(255,255,255,.1);--index-footer-menu-border-bottom-color:rgba(0,0,0,.3);--index-footer-menu-element-color:#a0a0a0;--index-footer-menu-bg-color:#222;--index-footer-menu-separator-color:#000;--virt-footer-bg-color:var(--index-navbar-bg-color);--virt-table-border-color:#727272;--virt-table-text-color:#727272;--virt-table-hover-bg-color:var(--rowhighlight-color);--virt-table-same-color:#444;--virt-highlight-color:var(--highlight-color);--virt-link-color:var(--link-color);--virt-link-hover-color:var(--index-link-hover-color)}.dark-mode #listen_txt:before,.dark-mode .reverseicon,.dark-mode .searchicon{filter:hue-rotate(165deg) invert(100%)}.dark-mode #accentSelection{background-image:url("data:image/svg+xml;utf8,<svg fill='%23bcbccc' height='24' viewBox='0 0 24 24' width='24' xmlns='http://www.w3.org/2000/svg'><path d='M7 10l5 5 5-5z'/><path d='M0 0h24v24H0z' fill='none'/></svg>")}.dark-mode .annIcon{filter:invert(1);-webkit-filter:invert(1)}.dark-mode .tooltip svg{filter:invert(1);-webkit-filter:invert(1)}@media(min-width:770px){.dark-mode .WRD tr:hover td.ToWrd>i.copy,.dark-mode .WRD span.zhgroup:hover>i.copy{filter:hue-rotate(165deg) invert(100%)}}:root{--control-text-color:#333;--control-bg-color:#d7d7d7;--control-border-color:#dadada;--control-focus-bg-color:#dfdede;--control-focus-color:#333}.dark-mode{--control-text-color:#ddd;--control-bg-color:#333;--control-border-color:#555;--control-focus-bg-color:#444;--control-focus-color:#fff}button,select,input,textarea,#reverseBtnContainer,.inputcontainer{background-color:var(--control-bg-color);color:var(--control-text-color);border:1px solid var(--control-border-color);border-radius:3px}select{padding-left:4px}button:focus,select:focus,input:focus,textarea:focus,button:hover,select:hover,input:hover,textarea:hover,#reverseBtnContainer:hover,.inputcontainer:hover,#reverseBtnContainer:focus,.inputcontainer:focus{background-color:var(--control-focus-bg-color);color:var(--control-focus-color)}button:hover,select:hover,input:hover,#reverseBtnContainer:hover{cursor:pointer}input:hover,.inputcontainer:hover,textarea:hover{cursor:text}button,input[type=button]{padding:4px 10px}*{box-sizing:border-box}input::-moz-focus-inner{border:0;padding:0}span.b{font-weight:bold}span.ic,span.i,.bl{font-style:italic;color:var(--bold-color)}span.r{color:var(--red-color)}span.supr1{vertical-align:super;color:var(--bold-color)}span.ac{font-variant:small-caps;color:var(--red-color);font-weight:bold}div.trans{padding:0}ol.entry li{margin-top:5px}.hide{display:none}.clickable{cursor:pointer}.entrySeparator{margin-top:1em;margin-bottom:1em;border-bottom:1px solid var(--border-color)}.small1{font-size:x-small;display:inline-block}html{font-size:100%;overflow-y:scroll;-webkit-text-size-adjust:100%;-ms-text-size-adjust:100%}@font-face{font-family:'WR_Korean';src:local('-apple-system'),local('BlinkMacSystemFont'),local('Malgun Gothic'),local('맑은 고딕'),local('helvetica'),local('Apple SD Gothic Neo'),local('sans-serif');unicode-range:U+AC00-D7AF}@font-face{font-family:'WR_Japanese';src:local('Helvetica Neue'),local('Arial'),local('Hiragino Kaku Gothic ProN'),local('Hiragino Sans'),local('Meiryo'),local('sans-serif');unicode-range:U+3000-30FF,U+FF00-FFEF,U+4E00-9FAF}@font-face{font-family:'WR_Arabic';src:local('Calibri'),local('Muna'),local('KacstOne'),local('Geeza Pro');unicode-range:U+600-6FF}body{margin:0;font-size:12px;line-height:1.231;font-family:WR_Korean,WR_Japanese,WR_Arabic,-apple-system,BlinkMacSystemFont,"Segoe UI","Roboto",sans-serif;font-display:swap;background:var(--bg-color)}body{color:var(--body-text-color)}a{text-decoration:none;color:var(--link-color)}a:hover{text-decoration:underline}a:visited{color:var(--visited-link-color)}a img{border:0}.mobileblock{display:inline;padding-left:3px}.alwaysblock{display:block}input:-moz-placeholder{color:var(--placeholder-color)}*[placeholder]{padding-left:5px !important}a .listen_language,a.conjugate_link:visited{color:var(--gray-color)}.clickable ul li.last:after{content:''}.even{background-color:var(--highlight-color);vertical-align:top}.odd{vertical-align:top}:not(.even)+.even,:not(.odd)+.odd{border-top:1px solid var(--row-color)}:not(.even)+.even td,:not(.odd)+.odd td{padding-top:8px}input::-webkit-input-placeholder:focus,input::-webkit-input-placeholder:active{color:var(--placeholder-focus-color) !important}input:-moz-placeholder:focus{color:var(--placeholder-focus-color) !important}input:-ms-input-placeholder:focus{color:var(--placeholder-focus-color) !important}.centerChild{position:relative}.centerChild>div{position:absolute;top:50%;left:50%;transform:translate(-50%,-50%)}.hcenterChild{position:relative}.hcenterChild>div{position:absolute;left:50%;transform:translate(-50%,0)}#contenttable{content-visibility:auto;width:100%}#contenttable>tbody,#contenttable>tbody>tr{display:block}#contenttable>tbody>tr{display:flex;flex-wrap:nowrap}#contenttable>tbody>tr>td#leftcolumn,#contenttable>tbody>tr>td#centercolumn,#contenttable>tbody>tr>td#rightcolumn{flex:1;min-width:0}#contenttable>tbody>tr>td#leftcolumn{flex-basis:164px;max-width:164px;flex-grow:1}#contenttable>tbody>tr>td#centercolumn{flex-basis:530px;max-width:530px;flex-grow:3}#contenttable>tbody>tr>td#rightcolumn{flex-basis:304px;max-width:304px;flex-grow:1}#container,#footer{width:1002px}#container{margin:0 auto;margin-bottom:3px;border-radius:3px;min-width:300px}#scontainer{position:relative;width:1000px;margin:0 auto}#__asptrace{overflow:hidden}#__asptrace td:nth-child(2){overflow-wrap:anywhere}#header{background:var(--main-color);height:41px;line-height:38px;width:100vw;position:relative;left:50%;right:50%;margin-left:-50vw;margin-right:-50vw}.full-header{background:var(--main-color);height:41px;line-height:38px;width:100%}.header-content{width:1002px;margin:0 auto}#logo{color:var(--header-text-color);float:left;font-size:16px;white-space:nowrap}#logo a{color:var(--header-link-color);font-size:22px}#logo a span{color:var(--header-link-span-color)}#logo h1{color:var(--header-link-h1-color);font-size:12px;display:inline}#nav{color:var(--header-text-color);float:right;font-size:13px;padding-top:2px;overflow:hidden;white-space:nowrap;max-width:45%;text-overflow:ellipsis}#nav a{font-weight:bold;color:var(--header-link-color);font-size:13px}.content{margin-top:-5px;background-color:var(--content-bg-color);-webkit-border-radius:3px;-moz-border-radius:3px;border-radius:3px;border:1px var(--border-color) solid;overflow:hidden;clear:both}#contenttable{border-collapse:collapse}#rightcolumn,#leftcolumn,#centercolumn{vertical-align:top}#footer{font-size:11px;position:relative;padding-top:7px;padding-bottom:5px}.footer{width:100%}#leftcolumn{line-height:1.4;border-right:1px solid var(--border-color)}#leftcolumn ul{list-style-type:none}#left{padding-left:0;margin-top:0;font-size:12px}#left ul li{padding-right:1px;padding-left:4px}#left ul{padding-left:0;padding-right:1px}html[dir=rtl] #leftcolumn ul{padding-inline-start:0}html[dir=rtl] ul#WRlastseen{padding-inline-start:revert !important}ul#WRlastseen>li{overflow:hidden;text-overflow:ellipsis;max-width:164px}#wrsave{list-style-type:none}td .title1{font-size:13px;font-weight:bold;border-bottom:1px solid var(--border-color);margin-bottom:7px;padding-top:25px;padding-bottom:6px;padding-left:16px;color:var(--left-col-title1-color)}.FCboxes{margin-top:5px;margin-left:-5px;padding-top:7px;padding-left:10px;border-top:solid 1px var(--border-color)}.FCboxes>b.highlight{color:var(--red-color)}#rightcolumn{border-left:1px solid var(--border-color)}.wotd{position:relative;font-family:Arial;padding:20px 0 0 0;margin:50px auto;width:280px;border-radius:10px;border:1px solid var(--wotd-border-color);border-top:3px solid var(--wotd-border-top-color);background-color:var(--wotd-bg-color);box-shadow:0 7px 12px 0 var(--wotd-box-shadow-color)}#wotdCalendar{width:17px;height:16px;display:inline-block;padding-right:3px}#wotdTitle{font-size:18px;margin-top:13px}#wotdSubtitle{font-size:80%;margin:5px 0 10px 0}.wotdTerms>a,.wotdTerms>a:visited{color:var(--gray-color);font-size:18px;text-decoration:none}.wotdTerms>a:hover{color:var(--wotd-term-hover-color)}#wotdSubscribe{background-color:var(--ad-bg-color);font-size:16px;padding:10px;border-radius:0 0 10px 10px;width:100%;margin:0}.subscribeBtn{border:2px solid var(--main-color);border-radius:20px;padding:9px 7px;background:var(--main-color);color:var(--header-text-color);text-transform:uppercase;font-size:16px;cursor:pointer;font-weight:700;width:100%}.subscribeBtn:hover{border:2px solid var(--main-color);background:transparent;color:var(--main-color)}label.checkbox{display:inline-block;padding-left:15px;text-indent:-15px;font-size:14px}input.checkbox{width:15px;height:15px;padding:0;margin:0;vertical-align:bottom;position:relative;top:-1px}#AppStore,#GooglePlay{width:150px;height:46px;display:inline-block}table.rightcolumn{table-layout:fixed}#centercolumn{padding:0;-webkit-box-shadow:0 0 6px 0 var(--box-shadow-color);box-shadow:0 0 6px 0 var(--box-shadow-color)}#otherDicts,#FTintro,.FTsource,#articleHead,#noTransFound,#ErrorMessage,#postArticle{padding:0 20px;font-size:14px}#otherDicts{margin-bottom:40px}#ErrorMessage{margin-top:30px}#FTintro{padding-top:5px !important;padding-bottom:5px !important}.FTsource{padding-left:50px}.FTlist{padding-left:80px}#article a,#articleWRD a,#articleHead a,#noTransFound a{font-size:13px}#article p,#articleWRD p,#articleHead p,#noTransFound p{font-size:13px;margin-bottom:3px}div#article .noword p{font-size:14px}div#article p#noEntryFound{font-size:12px}div#article p.tobetranslated{font-size:12px}h1.headerWord,h3.headerWord{display:inline-block;font-family:Georgia,Times,"Times New Roman",serif;font-size:25px;margin:16px 16px 16px 0}h1.headerWord ar,h3.headerWord.ar{margin:16px 0 16px 16px}#adprimisvdu{width:512px;margin-left:5px;margin-bottom:20px !important}.showingFor{font-style:italic;margin-top:18px;margin-bottom:-15px}.showingFor.ar{font-size:120%;margin-bottom:-10px}#footerlink{display:none}div#eplinkContainer{text-align:right;padding-right:20px}html[dir=rtl] div#eplinkContainer{direction:ltr;text-align:left;padding-left:20px}html.phone div#eplinkContainer{display:none}#englishPageLink{margin-top:3px}#englishPageLink>span:first-child{position:relative;top:2px}#englishPageLink>span{padding-right:5px;display:inline-block}#englishPageLink svg path{fill:var(--body-text-color)}html.phone #loginLink{display:none}#loginLink{background-image:url("data:image/svg+xml,%3Csvg width='18px' height='18px' viewBox='0 0 24 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M13 15C13 15.5523 12.5523 16 12 16C11.4477 16 11 15.5523 11 15C11 14.4477 11.4477 14 12 14C12.5523 14 13 14.4477 13 15Z' stroke='%23323232' stroke-width='2'/%3E%3Cpath d='M15 9C16.8856 9 17.8284 9 18.4142 9.58579C19 10.1716 19 11.1144 19 13L19 15L19 17C19 18.8856 19 19.8284 18.4142 20.4142C17.8284 21 16.8856 21 15 21L12 21L9 21C7.11438 21 6.17157 21 5.58579 20.4142C5 19.8284 5 18.8856 5 17L5 15L5 13C5 11.1144 5 10.1716 5.58579 9.58579C6.17157 9 7.11438 9 9 9L12 9L15 9Z' stroke='%23323232' stroke-width='2' stroke-linejoin='round'/%3E%3Cpath d='M9 9V5C9 3.89543 9.89543 3 11 3H13C14.1046 3 15 3.89543 15 5V9' stroke='%23323232' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'/%3E%3C/svg%3E");background-repeat:no-repeat;background-position-x:left;background-position-y:center;padding-left:20px}#loginLink.moved{padding-left:20px !important;margin-left:10px}#loginLink.supporter{background-image:url('data:image/svg+xml,<%3Fxml version="1.0" encoding="utf-8"%3F><svg width="16px" height="16px" viewBox="0 0 28 28" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M20.75 3C21.0557 3 21.3421 3.13962 21.5303 3.3746L21.6048 3.48102L25.8548 10.481C26.0556 10.8118 26.0459 11.2249 25.8395 11.5435L25.7634 11.6459L14.7634 24.6459C14.3906 25.0865 13.7317 25.1159 13.3207 24.7341L13.2366 24.6459L2.23662 11.6459C1.98663 11.3505 1.93182 10.941 2.08605 10.5941L2.14522 10.481L6.39522 3.48102C6.55388 3.21969 6.82182 3.04741 7.1204 3.00842L7.25001 3H20.75ZM17.515 12H10.484L13.999 20.672L17.515 12ZM22.844 12H19.673L16.756 19.195L22.844 12ZM8.326 12H5.155L11.242 19.193L8.326 12ZM9.674 5H7.81101L4.775 10H8.245L9.674 5ZM16.246 5H11.753L10.324 10H17.675L16.246 5ZM20.188 5H18.325L19.754 10H23.224L20.188 5Z" fill="%23212121"/></svg>')}#loginLink.supporter.moved{background-image:url('data:image/svg+xml,<%3Fxml version="1.0" encoding="utf-8"%3F><svg width="18px" height="18px" viewBox="0 0 28 25" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M20.75 3C21.0557 3 21.3421 3.13962 21.5303 3.3746L21.6048 3.48102L25.8548 10.481C26.0556 10.8118 26.0459 11.2249 25.8395 11.5435L25.7634 11.6459L14.7634 24.6459C14.3906 25.0865 13.7317 25.1159 13.3207 24.7341L13.2366 24.6459L2.23662 11.6459C1.98663 11.3505 1.93182 10.941 2.08605 10.5941L2.14522 10.481L6.39522 3.48102C6.55388 3.21969 6.82182 3.04741 7.1204 3.00842L7.25001 3H20.75ZM17.515 12H10.484L13.999 20.672L17.515 12ZM22.844 12H19.673L16.756 19.195L22.844 12ZM8.326 12H5.155L11.242 19.193L8.326 12ZM9.674 5H7.81101L4.775 10H8.245L9.674 5ZM16.246 5H11.753L10.324 10H17.675L16.246 5ZM20.188 5H18.325L19.754 10H23.224L20.188 5Z" fill="%23212121"/></svg>')}#article p.EngInf{font-size:12px;padding-bottom:0;margin-bottom:5px}.inflections{font-size:13px;margin-left:10px}p.other_languages{line-height:1.5em;font-size:12px !important}#lista_link a{display:inline-block;margin-bottom:4px}#WHlinksmoved,#postLinksmoved,#WHlinks_forMobile{display:none}#WHlinks{padding-top:8px;padding-bottom:8px}#checkMonoMatch{display:block;font-size:14px !important;font-weight:700;margin:2em 0 1.5em 0;background:var(--search-bg-color);padding:10px;border:1px solid var(--link-color);border-radius:8px;text-align:center;text-decoration:none;color:var(--link-color)}#checkMonoMatch:hover,#checkMonoMatch:visited:hover{background:var(--link-color);color:var(--search-bg-color)}.col_link:hover{color:var(--header-hover-color)}#checkMonoMatch:visited,.col_link:visited{color:var(--link-color)}.dismissBox{display:flex;padding:4px}.dismissBox .txt-container{flex:1}.dismissBox .close-icon-container{flex:0 0 16px;cursor:pointer}.dismissBoxAnimate{opacity:1;max-height:999px;transition:all .2s ease-in-out}.dismissBoxHidden{opacity:0;max-height:0;transition:opacity .5s,max-height .5s .1s}.close-icon{cursor:pointer;stroke:var(--close-icon-stroke)}.close-icon line,.close-icon circle{stroke:var(--close-icon-circle-stroke)}.close-icon circle{fill:var(--main-color);fill-opacity:0;transition:.5s cubic-bezier(.165,.775,.145,1.02)}.close-icon:hover circle{fill-opacity:1}.close-icon:hover line{stroke:#fff}.WarnNote{display:flex;border:1px solid var(--warnnote-main-border-color);border-right:2px solid var(--warnnote-border-color);border-bottom:2px solid var(--warnnote-border-color);background-color:var(--warnnote-bg-color);cursor:default;font-size:13px;border-radius:5px;padding:7px 15px;margin-top:10px}.WarnNote a:hover{text-decoration:underline}.WarnNote .icon{margin-right:5px;margin-top:1px}.hithere{animation:hithere 1s ease 1}@keyframes hithere{30%{transform:scale(1.2)}40%,60%{transform:rotate(-20deg) scale(1.2)}50%{transform:rotate(20deg) scale(1.2)}70%{transform:rotate(0deg) scale(1.2)}100%{transform:scale(1)}}.selectedTerm,.otherTerm{position:relative;white-space:nowrap}.otherTerm{cursor:pointer;color:var(--link-color)}.otherTerm:hover{color:var(--rowhighlight-color)}.selectedTerm .arrow,.otherTerm:hover .arrow{position:absolute;margin-left:calc(50% - 7.5px);bottom:-2px;width:0;height:0;border-style:solid;border-width:0 7.5px 5px 7.5px}.otherTerm:hover .arrow{border-color:transparent transparent var(--rowhighlight-color) transparent}.selectedTerm .arrow{border-color:transparent transparent var(--selected-term-arrow-color) transparent}.inAltTermOnly{display:block !important;font-size:14px;text-align:center;padding:14px 20px 0 20px}.tooltip.inAltTermOnly{cursor:pointer}.tooltip.inAltTermOnly span{left:50px;bottom:37px !important;font-size:90%;width:350px !important}.tooltip.inAltTermOnly::before{left:50px;top:10px}#search,#searchPlaceholder{height:51px}#search{direction:ltr;background:var(--search-bg-color);position:static;-webkit-border-radius:3px;-moz-border-radius:3px;border-radius:3px;border:1px var(--border-color) solid}#search.addKBLink,#searchPlaceholder.addKBLink{height:59px}#search div#useKBLink{position:absolute;font-size:11px;left:185px;top:36px}#searchPlaceholder.visibleKBLink,#search.visibleKBLink{height:70px}#search input{background:var(--bg-color);border:1px solid var(--search-input-border-color);-moz-border-radius:3px;-webkit-border-radius:3px;border-radius:3px;height:32px;width:280px;font-size:20px;padding-right:2px}#search input:active,#search input:focus{color:var(--body-text-color)}#text_form{display:flex;float:left;margin-left:184px;margin-top:6px}#text_form input.button{border:0;width:12px;height:12px;cursor:pointer;background-position:5px;line-height:31px;vertical-align:bottom;background-image:none;position:relative;bottom:1px;padding:8px 7px 8px 7px}.inputcontainer{display:inline-block;text-align:center;margin-left:5px;border:solid 1px var(--border-color);line-height:35px;height:32px;border-radius:2px;cursor:pointer}label.custom-select{margin-left:5px;position:relative;display:inline-block}.custom-select select{height:100%;font-weight:bold !important;width:164px}.custom-select select,.custom-select select option,.custom-select select optgroup{font-weight:normal}.sticky{position:fixed !important;top:0;left:0;width:100% !important;z-index:100;box-shadow:0 3px 14px 0 var(--sticky-search-box-shadow)}.sticky #text_form{float:none}#kbd-logo-cell{display:none}audio:not([controls]){display:none}#listen_widget{color:var(--gray-color);background-color:var(--content-bg-color);font-size:12px;display:inline-block;white-space:nowrap;padding:3px 0 2px;border:1px solid var(--tag-border-color);-webkit-border-radius:3px;-moz-border-radius:3px;border-radius:3px;margin-left:0}#listen_txt{cursor:pointer}#listen_txt,.listen_language{top:-1px;padding:7px 7px 5px 0;position:relative;left:4px;text-transform:uppercase;border-right:1px solid var(--tag-border-color);margin-right:1em}#listen_widget a:hover,.conjugate_link:hover{text-decoration:none;font-weight:bold !important}#listen_widget{overflow:hidden;vertical-align:middle;margin-bottom:5px}#articleWRD .conjugate{font-size:1em;line-height:1}#dummyspan{display:none}#accentSelection{border:0;text-transform:uppercase;color:var(--gray-color);background:transparent;padding:2px 0 0 3px;position:relative;top:-1px;-webkit-appearance:none;-moz-appearance:none;background:transparent;background-image:url("data:image/svg+xml;utf8,<svg fill='black' height='24' viewBox='0 0 24 24' width='24' xmlns='http://www.w3.org/2000/svg'><path d='M7 10l5 5 5-5z'/><path d='M0 0h24v24H0z' fill='none'/></svg>");background-repeat:no-repeat;background-position-x:100%;background-position-y:0;padding-right:2rem;height:23px}.pronWR,.pronRH{font-size:14px;margin-left:6px !important}.pwrapper{border:none;display:inline-block}.tooltip.pronWidget{font-size:14px;white-space:normal;text-align:left}.tooltip.pronWidget span{width:225px !important;padding:7px 10px !important}.pronRH i{font-size:13px}.pr{margin:0}.more-pron-state,.more-pron-target{display:none}.more-pron-wrap>p.pr{display:inline}.more-pron-state:checked~.more-pron-wrap .more-pron-target{display:block}.more-pron-state:checked~.more-pron-wrap .more-pron-target.expand{display:inline}.more-pron-state~div .more-pron-trigger:before{content:'[ ▾more ]'}.more-pron-state:checked~div .more-pron-trigger:before{content:'[ ▴less ]'}.more-pron-trigger{cursor:pointer;display:inline-block;padding:0 .5em;color:var(--more-pron-trigger-color)}div.pinyin>div{display:inline-block;line-height:20px}span.simplified,span.traditional,span.pinyin,span.hiragana{font-size:10px;font-style:italic;font-weight:bold;border:1px solid var(--tag-border-color);border-radius:4px;color:var(--tag-text-color);padding:3px 4px;cursor:default}span.simplified.sm,span.traditional.sm,span.pinyin.sm,span.hiragana.sm{font-size:9px;padding:2px 2px}td.nums1{font-weight:bold;color:var(--main-color);vertical-align:top;text-align:right}td.roman1{font-weight:bold;color:var(--main-color);vertical-align:top;font-size:16px}span.roman1{font-weight:bold;color:var(--main-color);vertical-align:bottom}.conjugate_link{color:var(--gray-color);background-color:var(--content-bg-color);font-size:12px;display:inline-block;white-space:nowrap;padding:3px 0 2px;border:1px solid var(--tag-border-color);-webkit-border-radius:3px;-moz-border-radius:3px;border-radius:3px;margin-left:0}.conjugate_link{height:10px;font-variant:small-caps;vertical-align:bottom;padding:0 2px 2px 2px;line-height:.7;top:-1px;text-transform:none}div.conv{margin-left:20px}div.notConv{margin-left:0;padding-left:0;border-left:0}ul.hEntry{margin-left:-20px}.espb ul,.espl ul{list-style-type:none}table #right{padding-left:18px;margin-top:0}li.synonym{margin-left:auto}.thumbs{display:none}.engthes ul{list-style-type:none;padding-top:0;margin-top:0}.liSense{margin-left:-40px}span.syno:hover{text-decoration:underline}div.tags{display:inline;width:50%;float:right;font-style:italic}.clickable ul li.liSense ul li.synonym{display:inline-block;font-size:14px}.clickable ul li.synonym{display:inline-block;font-size:14px}.tags{color:#808080}.clickable ul li.synonym:after{content:', '}.reseta{font-weight:bold}.inps{font-size:12px;border:solid 1px #808080;background-color:#f0f0f0;padding-bottom:5px;padding-left:10px;width:80%}.inps label{font-weight:bold}.inps input{width:300px}.addterm{margin-top:5px}div#spellSug{margin-left:2px !important}#spellSug table{border-style:hidden;border-collapse:collapse}#spellSug td{border-width:0}.notfound{padding:2px;border-top:solid var(--border-color) 1px;border-bottom:solid var(--border-color) 1px;background-color:var(--content-bg-color);margin-top:5px}.wrcopyright{margin-left:20px}table.WRD{width:100%;border-collapse:collapse;border-top:solid 1px var(--border-color);border-bottom:solid 1px var(--border-color);cursor:pointer}.noTapHighlight{-webkit-tap-highlight-color:transparent}.noTapHighlight:focus{outline:none !important}tr.wrtopsection td{padding-bottom:12px;padding-top:12px;font-size:16px;text-align:center}#articleWRD p.note-othersideonly{margin-left:20px;font-size:12px}.noselect{-webkit-touch-callout:none;-khtml-user-select:none;-moz-user-select:none;-ms-user-select:none;user-select:none}.termCopy{color:var(--term-copy-color);text-decoration:underline;position:relative;display:inline-block}.termCopy>i.copy{background-image:url("data:image/svg+xml,%3Csvg version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'  width='12px' height='12px' viewBox='0 0 32 32' xml:space='preserve'%3E%3Cstyle type='text/css'%3E.blueprint_een%7Bfill:%23111918%3B%7D%3C/style%3E%3Cpath class='blueprint_een' d='M28 4h-2V1c0-0.552-0.448-1-1-1H4C3.448 0 3 0.448 3 1v27c0 0.552 0.448 1 1 1h3v2c0 0.552 0.448 1 1 1h20c0.552 0 1-0.448 1-1V5C29 4.448 28.552 4 28 4z M24 27H5V2h19V27z M27 30H9v-2h15c0.552 0 1-0.448 1-1V6h2V30z M20 9H9V8h11V9z M20 12H9v-1h11V12z M20 15H9v-1h11V15z M20 18H9v-1h11V18z M20 21H9v-1h11V21z'/%3E%3C/svg%3E");background-repeat:no-repeat;width:0;height:12px;display:inline-block;position:relative;opacity:.5;top:2px;transition:width .2s}.termCopy.show>i.copy{width:14px}.termCopy.show:hover>i.copy{opacity:1}.termCopy>span.copytt{font-size:12px;font-style:normal;font-weight:normal;position:absolute;opacity:.8;width:100px;color:var(--header-text-color);background-color:var(--body-text-color);text-align:center;border-radius:5px;padding:5px;left:0;top:-30px}.termCopy>span.ctmenu{display:flex;align-items:center;justify-content:space-around;position:absolute;opacity:.8;color:var(--header-text-color);background-color:var(--header-text-color);border:1px solid var(--copy-ctmenu-border);text-align:center;border-radius:5px;padding:5px;left:0;top:-70px;box-shadow:2px 2px 2px 1px rgba(0,0,0,.2)}.termCopy>span.ctmenu>span.ctarrow{width:0;height:0;border-left:4px solid transparent;border-right:4px solid transparent;border-top:4px solid var(--copy-ctmenu-border);position:absolute;top:57px;left:18px}.termCopy>span.ctmenu>.cticon{display:flex;flex-direction:column;width:40px;height:40px;margin:3px;cursor:pointer}.termCopy>span.ctmenu>.cticon>svg{height:20px}.termCopy>span.ctmenu>.cticon:hover>svg path{fill:var(--term-copy-ctmenu-icon-hover-color)}.termCopy>span.ctmenu>.cticon:active>svg{position:relative;top:1px;left:1px}.termCopy>span.ctmenu label{color:var(--copy-ctmenu-label-color);font-size:9px;word-break:keep-all;white-space:nowrap;padding-top:5px;cursor:pointer}tr.more td{border-bottom:1px solid var(--border-color)}.WRD td{padding:2px}.WRD td.FrWrd{padding-left:20px}.WRD td.ToWrd{color:var(--body-text-color);position:relative;padding-right:15px}del.noclick,strong.noclick{font-size:13px;cursor:default}.hiraganatxt{font-size:10px}td .ToEx,td.FrEx{color:var(--sentences-color);word-break:break-word}td.ToEx.Ar,td.FrEx.Ar{direction:RTL;font-size:120%}td.ToEx:not(.Ru){font-style:italic}span.Ar{font-size:120%}.To2{font-style:italic}.dsense{font-style:normal}html:not([dir="rtl"]) .dsense{float:right !important}html[dir="rtl"] .dsense{float:left !important}.ltr{direction:ltr}.notePubl{padding-left:20px !important;padding-right:20px !important}table.WRD .additional{border-top:solid 1px var(--border-color)}table.WRDrefl{border-bottom:0;margin-bottom:15px}.WRreporterror{width:100%;border-collapse:collapse;border-bottom:1px solid var(--border-color);margin-bottom:40px}.WRreporterror td{padding-left:2px;padding-right:4px}a.conjugate{margin-left:.3em}.langHeader{font-size:13px;text-decoration:underline;font-weight:bold}.langHeader td{padding-bottom:4px}.POS2{color:var(--link-color)}.hw-flex-container{display:block}#termWithTashkeel{display:inline-block;direction:ltr;font-size:16px;padding-left:0;margin:0;margin-left:18px !important;margin-bottom:10px;cursor:pointer}.NoteInfl{font-size:12px;color:#808080}dl.ListInfl{display:table-row;margin:0}dt.ListInfl{display:table-cell;min-width:80px;text-align:right;padding-right:3px}dt.ListInfl::after{content:":"}dd.ListInfl{display:table-cell;padding-left:15px}ul.subEnt,.subEnt ul,.subEntry ul{margin-top:0;margin-bottom:0;padding-bottom:0}.subEntry span{display:inline}.forum{text-overflow:ellipsis;overflow:hidden}#forumapi{background-repeat:no-repeat;float:right;margin-top:15px;margin-right:9px;white-space:nowrap;font-size:12px}#forumapi span.bttn a{font-size:14px;font-weight:bold;color:var(--body-text-color);margin-right:-4px;padding:7px;border:1px solid var(--border-color);background:var(--content-bg-color)}#forumapi span.forum a{-webkit-border-top-left-radius:5px;-webkit-border-bottom-left-radius:5px;-moz-border-radius-topleft:5px;-moz-border-radius-bottomleft:5px;border-top-left-radius:5px;border-bottom-left-radius:5px}#forumapi span.api a{-webkit-border-top-right-radius:5px;-webkit-border-bottom-right-radius:5px;-moz-border-radius-topright:5px;-moz-border-radius-bottomright:5px;border-top-right-radius:5px;border-bottom-right-radius:5px}p#threadsHeader{font-size:13px !important;font-weight:bold;margin-bottom:0;padding:7px 0;border-top:1px solid var(--border-color)}p#threadsHeader.noborder{border-top:none}p.threadsLanguageSection{font-weight:bold;margin-bottom:3px}p.threadsLanguageSection>span.Ar{font-size:120%}#lista_link{margin-bottom:5px;padding-left:30px;padding-top:13px}#lista_link ul li{list-style-type:none;direction:ltr}#lista_link ul{padding-left:0;margin-bottom:5px}.threadnote{margin-bottom:30px;margin-top:15px;font-weight:bold}.threadnote ol{font-weight:normal;padding-top:2px;padding-bottom:2px}#extra_links{margin-bottom:15px;margin-left:43px}.extra_links{margin-bottom:15px;margin-left:15px;margin-top:10px}#extra_links a,.extra_links a{display:list-item;padding:2px 0}#extra_links .boxed.last,.extra_links .boxed.last{border:none !important}#extra_links a:last-child .boxed,.extra_links a:last-child .boxed{border-bottom:0 none}#forumNotes{display:none;margin:5px 0 25px 0}#forumNotes{font-size:14px !important;font-style:italic;font-weight:bold}#ad1{position:static;width:728px;height:86px;margin:6px auto;display:block}#top728{border:0 none;height:90px;overflow:hidden;width:100%}#ad2{position:static;width:728px;height:90px;margin:6px auto}td.ad{padding-bottom:10px}td.ad a{display:inherit}.us300c{text-align:center}#WRmobile{text-align:center}#gtrans{display:inline-block;border:0 none}input::placeholder{color:var(--input-placeholder-color)}::-webkit-input-placeholder{color:var(--input-placeholder-color)}::-moz-placeholder{color:var(--input-placeholder-color);opacity:1}:-ms-input-placeholder{color:var(--input-placeholder-color)}::-webkit-input-placeholder{color:var(--input-placeholder-color)}::-moz-placeholder{color:var(--input-placeholder-color)}:-ms-input-placeholder{color:var(--input-placeholder-color)}.noword>p{font-size:14px !important}table.WRDrefl{border-bottom:none;margin-bottom:15px}.super{color:var(--red-color);vertical-align:super;font-size:.8em}span.super:hover{text-decoration:none !important}#articleWRD .wrcopyright{font-size:10px}.notePubl_tr{border:1px solid var(--body-text-color);border-right:2px solid var(--body-text-color);border-left:2px solid var(--body-text-color)}#tabRev span,#tabRev a{width:auto}#postLinks{border-top:1px solid var(--border-color);border-bottom:1px solid var(--border-color);margin-top:15px;padding:10px 7px !important;border:1px solid var(--border-color);border-radius:5px;margin-bottom:15px;position:relative}#postLinks>span{font-size:13px !important;font-weight:700;position:absolute;left:10px;top:-10px;background-color:var(--content-bg-color);padding:0 4px}#postLinks a{font-size:13px}html[dir=rtl] #postLinks>span{right:10px}#listen_txt:before,.col_link,#wotdCalendar,#AppStore,#GooglePlay,#search .inputcontainer>i{background:url(/images/sprite_2022.webp?v=1);background-size:160px 172px}.webpNoSupp #listen_txt:before,.webpNoSupp .col_link,.webpNoSupp #wotdCalendar,.webpNoSupp #AppStore,.webpNoSupp #GooglePlay,.webpNoSupp #search .inputcontainer>i{background:url(/images/sprite_2022.png?v=2);background-size:160px 172px}.col_link{background-position:-92px -117px;width:16px;height:16px;display:inline-block !important;content:' '}.col_link:hover{filter:hue-rotate(40deg)}#listen_txt:before{background-position:-5px -117px !important;width:23px;height:16px;display:inline-block;content:' ';margin-right:4px;vertical-align:middle;margin-left:4px;margin-bottom:2.5px;position:relative;top:-1px}#search .inputcontainer>input{position:relative;background:none;top:-4px;left:-1px;width:30px;height:32px;cursor:pointer;padding:0;vertical-align:middle;border:none !important;line-height:33px}#search .inputcontainer>i{position:absolute;pointer-events:none;z-index:1}#search .inputcontainer>i.searchicon{background-repeat:no-repeat;background-position:-118px -118px !important;width:16px;height:16px;margin-top:7px;margin-left:6px}#search .inputcontainer>i.reverseicon{background-position:-65px -118px !important;background-repeat:no-repeat;width:17px;height:16px;margin-top:7px;margin-left:6px}#search #searchBtn:active,#search #reverseBtn:active{background-color:#b7b7b7}.FrWrd .engusg:before{content:"💬";vertical-align:middle;margin-right:3px}.adtitle{height:16px}#ad_728{position:absolute;color:transparent}.heavyUser:hover{border:1px solid var(--heavy-user-hover-border-color)}.heavyUser{background-color:var(--heavy-user-bg-color);width:70%;text-align:center;font-weight:bold;margin:3vh 0 1vh 0;border-radius:10px;padding:10px;border:1px solid var(--tag-border-color)}.extras{margin-top:2vh;border-radius:10px;padding:10px}.extras div:nth-child(n+2){margin-top:10px}.extras .extra_category{font-weight:bold}.WRD tr td:nth-child(2):not(.FrEx):not(.ToEx){width:40%}.WRD tr td:nth-child(1):not(.FrEx):not(.ToEx){width:24%}.WRD tr td:nth-child(3):not(.FrEx):not(.ToEx){width:36%}.WRD td.FrWrd{padding-left:5px}.WRD td.ToWrd{padding-right:1px;padding-left:5px}html[dir="rtl"] .WRD td.FrWrd{padding-right:5px}html[dir="rtl"] .WRD td.ToWrd{padding-right:5px;padding-left:1px}.loader,.loader:after{border-radius:50%;width:12px;height:12px}.loader{display:inline-block;top:2px;font-size:10px;position:relative;text-indent:-9999em;border-top:.3em solid var(--loader-border-top-color);border-right:.3em solid var(--main-color);border-bottom:.3em solid var(--main-color);border-left:.3em solid var(--main-color);-webkit-transform:translateZ(0);-ms-transform:translateZ(0);transform:translateZ(0);-webkit-animation:load8 1.1s infinite ease;animation:load8 1.1s infinite ease}@-webkit-keyframes load8{0%{-webkit-transform:rotate(0deg);transform:rotate(0deg)}100%{-webkit-transform:rotate(360deg);transform:rotate(360deg)}}@keyframes load8{0%{-webkit-transform:rotate(0deg);transform:rotate(0deg)}100%{-webkit-transform:rotate(360deg);transform:rotate(360deg)}}.table{display:table;border-collapse:separate;width:100%}.table>.row{display:table-row}.table>.row>.cell{display:table-cell}.adbackground{color:var(--header-text-color);background-color:var(--ad-placeholder-bg);text-align:center;vertical-align:middle;line-height:280px;width:100%}html.phone #articleHead,html.phone #noTransFound{padding:0 !important}html.phone h1.headerWord,html.phone h3.headerWord{margin:5px 16px 5px 10px}html.phone h1.headerWord.ar,html.phone h3.headerWord.ar{margin:5px 16px 5px 10px}html.phone .hw-flex-container{padding-left:10px;padding-right:10px}html.phone #WHlinks{display:none}html.phone #WHlinksmoved,html.phone #postLinksmoved{display:block}html.phone #WHlinksmoved a,html.phone #postLinksmoved a{display:block;font-size:1.5em;border-bottom:solid 1px var(--border-color);margin-top:0;margin-bottom:0;padding-left:10px;padding-top:12px;padding-bottom:12px}html.phone #WHlinksmoved>a:first-child{border-top:solid 1px var(--border-color);margin-top:-.5px}html.phone #WHlinksmoved a:active,html.phone #WHlinksmoved a:focus,html.phone #WHlinksmoved a:hover{text-decoration:none}html.phone #postLinks{display:none}#translation.swiper-slide{margin:0;padding:0}#definition.swiper-slide{margin:0;padding:5px}#synonyms.swiper-slide{margin:0;padding:5px}#mobiletop{padding:0 !important;margin-top:var(--ad-mobiletop-margin) !important}span.tracecontent th{padding:0 8px}span.tracecontent th.alt{padding:0 8px}span.tracecontent td{padding:0 8px}span.tracecontent h1,span.tracecontent h2,span.tracecontent h3{margin:2px 0}#tryMeMsg{color:var(--try-me-msg-color);height:16px;float:right;font-size:10px;margin-top:12px;margin-right:3px;opacity:0;cursor:default;transition:all .3s ease-in-out}#tryMeMsg.firstTime{display:block;opacity:1}#darkModeControls{height:16px;margin-top:10px;margin-right:-10px}#darkModeControls>.icon{width:16px;height:16px;cursor:pointer;opacity:.5;transition:all .3s ease-in-out}#darkModeControls>.icon:hover{opacity:1}#darkModeControls>.icon.lightmode,#darkModeControls>.icon.darkmode,#darkModeControls>.icon.automode{display:none}#darkModeControls>.icon path{fill:var(--dark-mode-icon-path-fill-color)}#darkModeControls>.icon.firstTime path{fill:var(--dark-mode-icon-path-fill-first-time-color);animation:updown 3s ease 6}@keyframes updown{0%,50%,100%{transform:translatey(0)}20%{transform:translatey(5px)}25%{transform:translatey(-20px)}30%{transform:translatey(20px)}35%{transform:translatey(-5px)}}_:-ms-lang(x),#reverseBtnContainer{display:none}tr.even:hover,tr.odd:hover,tr.evenEx:hover,tr.oddEx:hover{background-color:var(--rowhighlight-color) !important}.debugmsg{color:#fff;border-radius:3px;margin:10px;padding:3px}.debugmsg.warn{background-color:#f00}.debugmsg.info{background-color:#008000}@media screen and (max-width:1002px){#__asptrace,#container,#scontainer,#footer,.header-content{width:100%}#header,.full-header{left:0;right:0;margin-left:0;margin-right:0}#logo{margin-left:0;padding-left:12px}#nav{margin-right:0;padding-right:12px}}@media(min-width:769px){#adprimisvdu>div[id^="google_ads_iframe_"]{width:430px;margin-left:auto;margin-right:auto}}@media screen and (max-width:769px){#search div#useKBLink{position:absolute;font-size:11px;left:7px;top:31px}#search.addKBLink,#searchPlaceholder.addKBLink{height:49px}#search.visibleKBLink,#searchPlaceholder.visibleKBLink{height:62px}}@media(min-width:769px){.sticky #forumapi{margin-top:-25px}}@media screen and (max-width:769px){div.pinyin{margin:10px 10px 4px 10px}}@media(min-width:770px){.zhgroup,.jagroup{display:block;float:left;width:100%}.WRD td.ToWrd i.copy{opacity:.3;transition:opacity .2s}.WRD tr:hover td.ToWrd>i.copy,.WRD span.zhgroup:hover>i.copy,.WRD span.jagroup:hover>i.copy{background:url(/images/sprite_2022.webp?v=1);background-size:160px 172px;background-repeat:no-repeat;background-position:-138px -119px;position:absolute;width:16px;height:16px}html:not([dir="rtl"]) .WRD tr:hover td.ToWrd>i.copy,.WRD span.zhgroup:hover>i.copy,.WRD span.jagroup:hover>i.copy{right:5px}html[dir="rtl"] .WRD tr:hover td.ToWrd>i.copy{left:5px}.WRD tr:hover td.ToWrd>i.copy:hover,.WRD span.zhgroup:hover>i.copy:hover,.WRD span.jagroup:hover>i.copy:hover{opacity:1}.WRD tr:hover td.ToWrd>i.copy:active,.WRD span.zhgroup:hover>i.copy:active,.WRD span.jagroup:hover>i.copy:active{background-position:-137px -118px}.webpNoSupp .WRD tr:hover td.ToWrd>i.copy,.webpNoSupp .WRD span.zhgroup:hover>i.copy,.webpNoSupp .WRD span.jagroup:hover>i.copy{background:url(/images/sprite_2022.png?v=2);background-size:160px 172px}}@media only screen and (min-device-width:320px) and (max-device-width:480px) and (-webkit-min-device-pixel-ratio:2) and (orientation:portrait){#listen_txt,.listen_language{font-size:16px !important}}@media only screen and (max-width:769px){.FrWrd .engusg{margin-right:4px;font-size:19px !important;vertical-align:middle}}@media only screen and (max-width:768px){.adtitle{display:none}}@media screen and (max-width:800px){#forumapi{display:none}}@media screen and (max-width:769px){#ad1,#ad1_holder,#ad2,#logo h1,#nav,.OxAd,.eslinks,.mobileremove,td#rightcolumn,#audiodrop a:nth-child(n+3){display:none}.small1{font-size:small}.content{min-width:inherit;border:0;margin-top:0}#content{margin-bottom:0}.mobileblock{display:block;font-size:1.5em;border-bottom:solid 1px var(--border-color);margin-top:0;margin-bottom:0;padding-left:10px;padding-top:12px;padding-bottom:12px}#footer>a.mobileblock:first-child{border-top:solid 1px var(--border-color);margin-top:-.5px}#footer>a.mobileblock:first-child{margin-top:-1px}#header,.full-header,.content{width:auto}#contenttable{width:100%}#leftcolumn,#centercolumn,#rightcolumn{max-width:100% !important}#footer{margin-top:0;padding-top:0}.mobileblock:active,.mobileblock:focus,.mobileblock:hover{text-decoration:none}#logo{padding-left:10px;margin-left:0}#container,#scontainer,#footer,#__asptrace,.header-content{width:100%}#container{word-wrap:break-word;word-break:break-word}#otherDicts,#FTintro,.FTsource,#postArticle{padding:0 3px}#postArticle{padding:0 !important}#postArticle>*:not(.mobileAd_holderContainer):not(#lista_link){padding:0 3px 0 10px}#pronunciation_widget{margin-left:10px}.first{border-top:solid 1px var(--border-color);padding-left:0}#postArticle{width:inherit;padding-left:10px}#article>*:not(.mobileAd_holderContainer){padding-left:10px}#centercolumn{width:auto}#spellSug table{margin-top:1em}#spellSug td{padding:0}#spellSug td:not(:last-child){padding-right:15vw}#spellSug a{line-height:10vw;font-size:16px !important}#spellSug,#noEntryFound{font-size:16px;padding-left:10px !important}#otherDicts,#FTintro,.FTsource,.virtual-article{font-size:19px}#footerlink a{font-variant:small-caps;font-size:18px !important}#footerlink{display:block;margin-right:10px;float:right;padding-top:10px}.FTlist,.FTsource{padding-left:0;padding-right:0}.FTsource{margin-top:12px}#text_form{left:auto;margin-left:auto;margin-top:2px;float:none}#search{height:auto;width:inherit;padding-left:3px;padding-top:3px;padding-bottom:3px}#search{width:auto}#articleWRD{padding:0}#articleWRD{width:inherit}#articleWRD{font-size:16px}.WRD td.FrWrd{padding-left:10px}.WRD td.ToWrd{padding-right:1px}#collinsdiv{font-size:16px}.noword{margin:0 10px}}@media only screen and (max-device-width:300px){.WRD td.FrWrd{padding-left:1px}#articleWRD{font-size:15px}table.WRD{width:100vw}#otherDicts,#FTintro,.FTsource{font-size:16px}ul #tabWR{margin-left:0 !important}#centercolumn div#collinsdiv{padding:0 !important}}@media only screen and (max-device-width:560px){p.other_languages{margin-top:2vh}p.other_languages a{font-size:1.2em;margin-right:1.5vw;margin-left:1.5vw}.footer td{height:30px;vertical-align:bottom;padding:0 8px}#englishPageLink span{height:16px}#englishPageLink svg{width:16px;height:16px}.WRreporterror td{height:30px;vertical-align:bottom}.FTlist a{font-size:1.3em;margin-right:.5vw;margin-left:.5vw}#lista_link a{font-size:1.3em}#extra_links,.extra_links{margin-top:2vh}}@media screen and (max-width:769px){td#leftcolumn{display:none}#text_form .inputcontainer{width:32px;height:31px}label.custom-select{margin-right:2px;height:31px}#search{height:41px}#search input[type='search']{width:100%}#search #reverseBtnContainer{margin-left:0}#text_form{display:flex;padding:0 5px 0 5px;align-items:center;width:100%}#myAutoComplete{width:calc(100% - 238px)}}@media all and (-ms-high-contrast:none){#reverseBtnContainer{display:none}}@media screen and (min-width:0\0){#reverseBtnContainer{display:none}}
        :root{--ac-text-color:#333;--ac-bg-color:#fff;--ac-border-color:#ccc;--ac-shadow-color:rgba(0,0,0,.1);--ac-separator-color:#dcdcdc;--ac-sugg-bold-color:#1f8dd6;--ac-sugg-text-color:#fff;--ac-sugg-active-bg-color:#5e58c7;--ac-sugg-hover-bg-color:#5e58c7;--ac-sugg-hover-text-color:var(--ac-sugg-text-color)}.autocomplete-suggestions{font-size:12px;text-align:left;cursor:default;background:var(--ac-bg-color);border:1px solid var(--ac-border-color);border-top:0;box-shadow:1px 2px 5px 5px var(--ac-shadow-color);position:absolute;display:none;z-index:9999;box-sizing:border-box}.autocomplete-suggestion{position:relative;padding:0 .6em;line-height:23px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;font-size:1.02em;color:var(--ac-text-color);border-top:solid 1px var(--ac-separator-color);cursor:pointer}.autocomplete-suggestion.ar{direction:rtl;text-align:right}.autocomplete-suggestion.ar>span.ar{font-size:120%}.autocomplete-suggestion b{font-weight:400;color:var(--ac-sugg-bold-color)}.autocomplete-suggestion a{display:none}.autocomplete-suggestion.hover{background:var(--ac-sugg-hover-bg-color);color:var(--ac-sugg-hover-text-color)}.autocomplete-suggestion.hover a{display:block;color:var(--ac-sugg-hover-text-color)}@media screen and (max-width:769px){.autocomplete-suggestion{font-size:1.6em;line-height:40px !important;padding:.2em .6em}.autocomplete-footer,.autocomplete-header{font-size:1.5em;line-height:40px !important;padding:.2em 2.2em !important}.autocomplete-suggestion:active,.autocomplete-footer:active{background:var(--ac-sugg-active-bg-color);color:var(--ac-sugg-text-color)}.actips{margin-right:-32px !important;margin-top:10px !important;display:inline-block;line-height:15px}}.autocomplete-suggestions>.autocomplete-footer{font-weight:700;font-style:italic;border-bottom:1px solid var(--ac-separator-color);position:relative;padding:0 2.4em;line-height:23px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;color:var(--ac-text-color);border-top:solid 1px var(--ac-separator-color);cursor:pointer}.autocomplete-suggestions>.autocomplete-footer.hover{background:var(--ac-sugg-hover-bg-color);color:var(--ac-sugg-hover-text-color)}.autocomplete-suggestions>.autocomplete-header{display:flex;justify-content:space-between;align-items:center;font-weight:700;padding-left:2.4em;padding-top:.2em;padding-bottom:.2em;border-bottom:1px solid var(--ac-separator-color);color:var(--ac-text-color)}.lang{background-color:#b7b7b7;color:#fff;font-weight:bold;padding:1px;width:50px}.dark{background-color:#878787}.ACconj{float:right}#si{-webkit-transition:background .1s ease-in-out !important;transition:background .1s ease-in-out !important}.dict,.dict:focus{padding-left:22px !important;font-size:18px !important;background:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='16' height='16' fill='currentColor' class='bi bi-book' viewBox='0 0 16 16'%3E%3Cpath d='M1 2.828c.885-.37 2.154-.769 3.388-.893 1.33-.134 2.458.063 3.112.752v9.746c-.935-.53-2.12-.603-3.213-.493-1.18.12-2.37.461-3.287.811V2.828zm7.5-.141c.654-.689 1.782-.886 3.112-.752 1.234.124 2.503.523 3.388.893v9.923c-.918-.35-2.107-.692-3.287-.81-1.094-.111-2.278-.039-3.213.492V2.687zM8 1.783C7.015.936 5.587.81 4.287.94c-1.514.153-3.042.672-3.994 1.105A.5.5 0 0 0 0 2.5v11a.5.5 0 0 0 .707.455c.882-.4 2.303-.881 3.68-1.02 1.409-.142 2.59.087 3.223.877a.5.5 0 0 0 .78 0c.633-.79 1.814-1.019 3.222-.877 1.378.139 2.8.62 3.681 1.02A.5.5 0 0 0 16 13.5v-11a.5.5 0 0 0-.293-.455c-.952-.433-2.48-.952-3.994-1.105C10.413.809 8.985.936 8 1.783z'/%3E%3C/svg%3E") 5px center no-repeat,linear-gradient(180deg,#c7c5f0,#fff,#fff) !important;color:#333 !important}.actips,.actips:visited{margin-right:5px;margin-top:0;border:none;border-radius:3px;font-size:9px;width:14px;height:14px}.actips path{fill:#878787}.actips:hover path{fill:#1f8dd6}.actips>svg{pointer-events:none}#fSelect{transition:all .1s ease-in-out}#fSelect.shake{animation:zoom-in-zoom-out .15s;box-shadow:rgba(0,0,0,.4) 0 0 8px 0}@keyframes zoom-in-zoom-out{0%{transform:scale(1,1)}50%{transform:scale(1.01,1.01)}100%{transform:scale(1,1)}}@media only screen and (min-device-width:320px) and (max-device-width:480px) and (-webkit-min-device-pixel-ratio:2) and (orientation:portrait){.actips{line-height:28px}}
        .tooltip{position:relative;display:inline-block;cursor:pointer}.tooltip span:not(.noTooltip),.tooltip::after{visibility:hidden;opacity:0;transition:opacity .3s ease-in-out,left .3s ease-in-out;z-index:9999}.tooltip span:not(.noTooltip){background-color:#000;width:240px;color:#eee;text-align:center;border-radius:6px;padding:12px;position:absolute;bottom:calc(100% + 6px);left:50%;margin-left:-120px;line-height:1.4;box-shadow:0 2px 8px rgba(0,0,0,.2)}.tooltip:hover::after{content:'';position:absolute;bottom:auto;top:0;left:50%;margin-left:-6px;border-width:6px;border-style:solid;border-color:#000 transparent transparent transparent}html[lang="ar"] .tooltip:hover::after{margin-left:-12px}.tooltip:hover span:not(.noTooltip),.tooltip:hover::after{visibility:visible;opacity:.8}.tooltip.down:hover::after{top:calc(100% - 8px);bottom:0;top:auto;border-color:transparent transparent #000 transparent}@media only screen and (max-width:480px){.tooltip span:not(.noTooltip){width:180px;left:50%;margin-left:-90px}.tooltip span:not(.noTooltip)::after{left:50%;margin-left:-6px}}.tooltip.tooltipvirtual span:not(.noTooltip){white-space:nowrap;padding:10px 15px;width:auto}
        .modal{opacity:0;display:none;position:fixed;z-index:999;padding-top:100px;left:0;top:0;width:100%;height:100%;overflow:auto;background-color:var(--modal-fallback-background-color);background-color:var(--modal-background-color);transition:all 150ms ease-in-out}.modal-content{text-align:left;opacity:0;background-color:var(--modal-content-background-color);margin:auto;margin-top:-20px;padding:20px;border:1px solid var(--modal-border-color);width:80%;-webkit-box-shadow:5px 9px 15px 5px var(--modal-box-shadow-color);box-shadow:5px 9px 15px 5px var(--modal-box-shadow-color);transition:all 150ms ease-in-out}.modal.show{opacity:1}.modal.show>.modal-content.show{opacity:1;margin-top:0}.close{color:var(--close-button-color);float:right;font-size:28px;font-weight:bold}.close:hover,.close:focus{color:var(--close-button-hover-focus-color);text-decoration:none;cursor:pointer}@media only screen and (min-device-width:320px) and (max-device-width:480px) and (-webkit-min-device-pixel-ratio:2) and (orientation:portrait){.modal-content{width:90%}}
        #stickyAdContainer{position:fixed;text-align:center;bottom:0;min-height:50px;width:100%;visibility:visible !important;z-index:2147483647;background:#fafafa !important}#stickyAdContainer:not(.startVisible){bottom:-107px}.wr-grip-icon{position:absolute;display:block !important;inset:auto !important;clear:none !important;width:100%;height:6px;margin:0 !important;max-height:none !important;max-width:none !important;opacity:1 !important;overflow:visible !important;-webkit-tap-highlight-color:transparent;background-color:#fafafa !important;box-shadow:rgba(0,0,0,.2) 0 -1px 5px -1px,rgba(0,0,0,.2) 0 1px 2px -1px !important}.wr-grip-icon svg{margin:0 !important;position:absolute !important;bottom:0 !important;left:0% !important;display:block !important;width:80px !important;height:27px !important;transform:none !important;pointer-events:initial !important}.wr-grip-icon svg path:not(.arrow){fill:#fafafa;stroke:#fafafa}.wr-grip-icon svg path.arrow{stroke:#616161}.wr-grip-icon span:last-child{width:14px}.wr-grip-icon span:first-child{font-size:12px;color:#000 !important;padding-right:5px}.wr-grip-icon circle{fill:#707070;stroke:#707070;fill-opacity:1}.stickyAdContent{margin-top:7px}.stickyAdContent iframe{min-width:320px;min-height:50px}#stickyAdContainer div.clickProtect{position:absolute;z-index:2147483647;left:0;top:0;right:0;bottom:0}#stickyAdContainer div.clickProtect.allow{pointer-events:none;z-index:-1}
        :root{--bullet-size:5px;--bullet-active-size:calc(var(--bullet-size) + var(--bullet-size)*.8)}.swiper-container{overflow:hidden;width:100%;max-width:100vw;position:relative}.swiper-wrapper{display:flex;flex-wrap:nowrap;transition:transform .2s ease-in-out;width:100%;box-sizing:border-box;height:100%}.swiper-slide{flex:0 0 100%;max-width:100vw;box-sizing:border-box;position:relative;display:flex;justify-content:center;height:100%}.swiper-content{width:100%;max-width:100vw;box-sizing:border-box;min-height:150px}.spinner{margin-top:100px;border:4px solid var(--swiper-spinner-border-color);width:36px;height:36px;border-radius:50%;border-left-color:var(--swiper-spinner-border-left-color);animation:spin 1s linear infinite;position:absolute;left:50%;margin-left:-18px;z-index:1}@keyframes spin{0%{transform:rotate(0deg)}100%{transform:rotate(360deg)}}.hidden{display:none}.error{color:var(--swiper-error-color);text-align:center}.swiper-pagination{display:flex;align-items:center;justify-content:flex-end;height:var(--bullet-active-size);padding-right:2px;margin-top:5px;margin-bottom:5px}.swiper-pagination-bullet{display:inline-block;width:var(--bullet-size);height:var(--bullet-size);margin:0 4px;background:var(--swiper-pagination-bullet-background);border-radius:50%;opacity:.3;cursor:pointer;transition:all .2s}.swiper-pagination-bullet:hover{background:var(--swiper-pagination-bullet-hover-background)}.swiper-pagination-bullet-active{width:var(--bullet-active-size);height:var(--bullet-active-size);opacity:.5}#headerTabs{background-color:var(--swiper-header-tabs-background-color);border-bottom:2px solid var(--swiper-header-tabs-border-bottom-color);overflow-x:auto;-webkit-overflow-scrolling:touch}#headerTabs::-moz-scrollbar{height:1px}#headerTabs::-webkit-scrollbar{height:1px}#headerTabs{scrollbar-width:none;scrollbar-color:transparent transparent}#headerTabs ul{display:flex;flex-wrap:nowrap;list-style:none;padding:0;margin:0}#headerTabs ul li{flex:0 0 auto;padding:7px 10px;cursor:pointer;transition:color .1s,border-bottom .1s;color:var(--swiper-header-tabs-color);border-bottom:3px solid transparent}#headerTabs ul li:hover{color:var(--header-tabs-hover-color);background-color:var(--swiper-header-tabs-hover-background-color)}#headerTabs ul li.selected{color:var(--swiper-header-tabs-selected-color);border-bottom:3px solid var(--swiper-header-tabs-selected-border-bottom-color);font-weight:bold}#headerTabs ul li.selected:hover{color:var(--swiper-header-tabs-selected-hover-color)}#headerTabs ul li a,#headerTabs ul li span{text-decoration:none;color:inherit;display:block}#headerTabs::-webkit-scrollbar{height:1px}#headerTabs::-webkit-scrollbar-thumb{background:var(--swiper-scrollbar-thumb-background)}#headerTabs::-webkit-scrollbar-thumb:hover{background:var(--swiper-scrollbar-thumb-hover-background)}#headerTabs::-webkit-scrollbar-track{background:var(--swiper-scrollbar-track-background)}@media(max-width:768px){#headerTabs ul li{font-size:12px}}
    </style>


<style type="text/css">
    /* sprite icons temporary fix */
    #listen_txt:before, .col_link, #wotdCalendar, #AppStore, #GooglePlay, #search .inputcontainer > i {
        background: url('/images/sprite_2022.webp?v=1');
        background-size: 160px 172px;
    }
    .webpNoSupp #listen_txt:before, .webpNoSupp .col_link, .webpNoSupp #wotdCalendar, .webpNoSupp #AppStore, .webpNoSupp #GooglePlay, .webpNoSupp #search .inputcontainer > i {
        background: url('/images/sprite_2022.png?v=2');
        background-size: 160px 172px;
    }
    .col_link { background-position: -92px -117px;}

    /* SECTION: BROWSER/PLATFORM RULES */
    /*#1055: headertabs not showing correctly when desktop view is used on a mobile phone*/
    /*Keep the tabs large enough for fingers and reduce the font size*/

	/* hack because iOS app is showing table in wrong sized text*/
	/*issue #989 (Listen box styling: speaker icon too high): Hack related to OSX*/
#listen_txt{ top: 1px !important}#accentSelection{ top: 1px !important}
	/*Desktop fixes*/
tr.even:hover, tr.odd:hover, tr.evenEx:hover, tr.oddEx:hover{background-color:var(--rowhighlight-color);}
	/*Ads fixes*/

	/* SECTION: CONDITIONAL LANGUAGE FILES */
    

    
    

    

    

    

    

	/* SECTION: OTHER DICTIONARIES RULES */
    

    

    

</style>



<script>
    var wrserver = {
  "Initialization": null,
  "ddict": {
    "dict": "esit",
    "dict_alt": "",
    "isDictionary": true,
    "isBase": false,
    "isMonolingual": false,
    "isVirtual": false,
    "isVirtualPlus": true,
    "isAutomatic": false,
    "isReversible": false,
    "showOtherSide": false,
    "hasOneSide": false,
    "addVirtualInGA": false,
    "isRightToLeft": false,
    "isAsian": false,
    "isWRDict": false,
    "isCollins": true,
    "isEspasa": false,
    "isMondadori": false,
    "isLarousse": false,
    "isLangenscheidt": false,
    "isConjugator": false,
    "forumIDs": "53",
    "defaultForumID": "53",
    "defaultForumName": "Italiano-Espa\u00F1ol",
    "IsValidDictionary": true,
    "dict_OppositeDirection": "ites",
    "term_count": 0,
    "collocation_count": 0,
    "translation_count": 0,
    "stats_last_updated": null,
    "note": "",
    "last_update": null
  },
  "ipcc": "US",
  "ipcc2": [
    "WA",
    ""
  ],
  "os": 1,
  "platform": 0,
  "browser": 0,
  "browserVersion": 0,
  "route": null,
  "IsVirtKeyboardNeeded": false,
  "servername": "wwwor1",
  "lineCount": {},
  "ad": {
    "AdMode": 0,
    "bGoogleOnly": false,
    "bUseParallelIntegration": false,
    "bEnableAmazon": false,
    "bEnablePrebid": false,
    "bEnableConfiant": false,
    "bPrebid": false,
    "bPrebid_forum": false,
    "bPrebid_728A": false,
    "bPrebid_300A": false,
    "bPrebid_300B": false,
    "bPrimis_OnexOne": false,
    "bPrebid_728F_top": false,
    "bPrebid_728F_mid": false,
    "bPrebid_728F_bot": false,
    "bPrebid_m320x50": false,
    "bPrebid_mf320x50": false,
    "bPrebid_m300x250": false,
    "bPrebid_728x90mt": false,
    "bPrebid_indep": false,
    "bPrebid_abtest": false,
    "au728A": null,
    "au728x90mt": null,
    "au300A": null,
    "au300B": null,
    "aum320x50": null,
    "aumf320x50": null,
    "aum300x250": null,
    "bNoAds": false,
    "useConsent": false,
    "errors": null,
    "isForum": false,
    "runABTest": false,
    "RandomClass": null,
    "RandomNumber": 0,
    "RandomNumber10000": 0,
    "bEnableLazyLoading": false,
    "bEnableSRA": false,
    "bEnableBlockThrough": false,
    "UseInlineCode": false,
    "IsTestAdPage": false,
    "auf728F_top": null,
    "auf728F_mid": null,
    "auf728F_bot": null,
    "bSnigelEnabled": true,
    "bSovrnEnabled": false,
    "bWREnabled": false,
    "bPrimisEnabled": false,
    "SnigelDesktopReqPercent": 45,
    "SnigelMobileReqPercent": 45,
    "PrimisDesktopReqPercent": 30,
    "PrimisMobileReqPercent": 0,
    "SovrnDesktopReqPercent": 5,
    "SovrnMobileReqPercent": 5
  },
  "wrTraceData": []
};
</script>


<!-- Favicon -->
<link rel="icon" href="/favicon.ico" sizes="any"><!-- 32×32 -->
<link rel="icon" href="/icon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="/apple-touch-icon.png"><!-- 180×180 -->
<link rel="manifest" href="/favicons/manifest.json?dict=esit">


<meta name="theme-color" content="#ffffff">

<script>var strOrig = "nevar"; var strDic = "esit";</script>

<script>
    function check_webp_feature(feature, callback) {
        var kTestImages = {
            lossy: "UklGRiIAAABXRUJQVlA4IBYAAAAwAQCdASoBAAEADsD+JaQAA3AAAAAA",
            lossless: "UklGRhoAAABXRUJQVlA4TA0AAAAvAAAAEAcQERGIiP4HAA==",
            alpha: "UklGRkoAAABXRUJQVlA4WAoAAAAQAAAAAAAAAAAAQUxQSAwAAAARBxAR/Q9ERP8DAABWUDggGAAAABQBAJ0BKgEAAQAAAP4AAA3AAP7mtQAAAA==",
            animation: "UklGRlIAAABXRUJQVlA4WAoAAAASAAAAAAAAAAAAQU5JTQYAAAD/////AABBTk1GJgAAAAAAAAAAAAAAAAAAAGQAAABWUDhMDQAAAC8AAAAQBxAREYiI/gcA"
        };
        var img = new Image();
        img.onload = function () {
            var result = (img.width > 0) && (img.height > 0);
            callback(feature, result);
        };
        img.onerror = function () {
            callback(feature, false);
        };
        img.src = "data:image/webp;base64," + kTestImages[feature];
    }
    check_webp_feature('alpha', function (feature, isSupported) {
        if (!isSupported) {
            // webp not supported,
            document.getElementsByTagName("html")[0].classList.add("webpNoSupp");
        }
    });
</script>

        
        
            <script defer src="/js/bundle.min.js?v=dFE_C4ge4zteO5Kp_S0zERmGCCo7e5ALaWC41exIwpI"></script>
        




    <script src="//btloader.com/tag?o=5749731276881920&upapi=true" async></script>
    <script>
        consoleDebug('>> BlockThrough enabled');
    </script>


<script>
    console.log(`>> Provider selection:
    snigel: True
    sovrn: False
    WR: False
    primis: False`);
</script>
</head>
<body>
    




    <header class="full-header">
        <div class="header-content">
            <div id="logo" >
                <a href="https://www.wordreference.com/">WordReference<span>.com</span></a><span class="mobileremove">  |  </span><h1><span>Dizionari</span> <span>di</span> <span>lingua</span> <span>online</span></h1>
            </div>

            <div id="nav" >
                    <a href="/esit/"><span>Dictionaries</span></a>
| <a href=""><span>nevar</span></a>            </div>
        </div>
    </header>


    <div id="ad1">

                    <!-- adngin-top_leaderboard-0 -->
                    <div id="adngin-top_leaderboard-0"></div>
                    </div>





    <script>
        function changeTheme(n,t){enableTheme(n);t&&saveDarkModeSettings(n)}function enableTheme(n){if(n==="dark")document.body.classList.add("dark-mode");else if(n==="auto"){const n=window.matchMedia("(prefers-color-scheme: dark)");n.matches?document.body.classList.add("dark-mode"):document.body.classList.remove("dark-mode")}else document.body.classList.remove("dark-mode")}function isForcedDarkMode(){const n=new URLSearchParams(window.location.search);return n.has("display")&&n.get("display")==="dark"}function loadDarkModeSettings(){if(isForcedDarkMode())return"dark";let t="sWRSettings";if("localStorage"in window&&window.localStorage!==null&&localStorage[t]!=null){var n=JSON.parse(localStorage[t]);return n.theme?n.theme:"light"}return"light"}function saveDarkModeSettings(n){var t={theme:"light"};let i="sWRSettings";"localStorage"in window&&window.localStorage!==null&&localStorage[i]!=null?(t=JSON.parse(localStorage[i]),t.theme=n,localStorage[i]=JSON.stringify(t)):(t={theme:n},localStorage[i]=JSON.stringify(t))}var currentTheme=currentTheme||loadDarkModeSettings();enableTheme(currentTheme);window.matchMedia("(prefers-color-scheme: dark)").addListener(function(n){n.matches&&currentTheme=="auto"?changeTheme("dark",!1):n.matches||currentTheme!="auto"||changeTheme("light",!1)});
    </script>


    <div id="container">
        

    <div id="searchPlaceholder" class="">
        <div id="search" class="">
            <div id="scontainer">
                <form method="GET" action="/redirect/translation.aspx" id="text_form" name="sbox" onsubmit="return toSubmit(event);">
                    <div id="myAutoComplete" style="display:inline">
                        <input type="search" name="w" id="si" title="shortcut: /" oninvalid="alert('Caractéres inválidos en el campo de búsqueda');" pattern="^[^<>%\\]*$" size="20" maxlength="200" tabindex="1" onKeyDown="keyDown(event)" value="" placeholder="Cerca" autocomplete="off" autocorrect="off" autocapitalize="none">
                        <div id="myACContainer" style="display:inline"></div>
                        <div id="tipsModal" class="modal">
                            <div class="modal-content">
                                <span class="close">&times;</span>
                                <div class="modal-body"></div>
                            </div>
                        </div>
                    </div>
                    <label class="custom-select">
                        <select size="1" name="dict" tabindex="2" id="fSelect">
                                <option value='esit' title='Spanish-Italian' selected>Español-Italiano</option>
                                <option value='ites' title='Italian-Spanish'>Italiano-Español</option>
                            <option id='dictseparator' class="separator" disabled>──────────</option> <!-- Separator -->
                                <option value='enes' title='English-Spanish'>Inglés-Español</option>
                                <option value='esen' title='Spanish-English'>Español-Inglés</option>
                                <option value='enit' title='English-Italian'>Inglés-Italiano</option>
                                <option value='iten' title='Italian-English'>Italiano-Inglés</option>
                                <option value='eses' title=''>Español: definición</option>
                                <option value='essin' title=''>Español: sinónimos</option>
                                <option value='esgram' title=''>Español: gramática</option>
                                <option value='itit' title=''>Definizione italiana</option>
                                <option value='other' title=''>altro...</option>
                        </select>
                    </label>
                    <div id="reverseBtnContainer" class="inputcontainer">
                        <i class="reverseicon"></i>
                        <input type="button" id="reverseBtn" title="" tabindex="3" value="" />
                    </div>
                    <div class="inputcontainer">
                        <i class="searchicon"></i>
                        <input type="submit" id="searchBtn" name="B" title="Cerca" tabindex="4" value="">
                    </div>

                    <script>
                        function toSubmit(event) {
                            if(document.sbox.w.value.slice(0,1) == ":"){
                                console.log("** I can't submit when it's a shortcut.");
                                event.preventDefault();
                                return false;
                            }

                            if(document.sbox.dict.value=='esit'){
                                location.href = '/esit/' + document.sbox.w.value;
                                return(false);
                            }
                        }
                    </script>
                </form>

                <div id="forumapi">
                    <span class="forum api bttn"><a href="https://forum.wordreference.com">Foros</a></span>
                </div>
            </div>
        </div>
    </div>


        <div class="content">
            <table id="contenttable" >
                <tr>
                    
<td id="leftcolumn">
    <ul id="left" class="leftcolumn">
        <li>
            

<ul>
    <li class="title1" title="See Also:">Ver También:</li>
</ul>
<ul>
    <li id="link" ><ul><li><a href="/esit/neurosis">neurosis</a></li>
<li><a href="/esit/neur%C3%B3tico">neurótico</a></li>
<li><a href="/esit/neutral">neutral</a></li>
<li><a href="/esit/neutralice">neutralice</a></li>
<li><a href="/esit/neutralidad">neutralidad</a></li>
<li><a href="/esit/neutralizar">neutralizar</a></li>
<li><a href="/esit/neutro">neutro</a></li>
<li><a href="/esit/neutr%C3%B3n">neutrón</a></li>
<li><a href="/esit/nevada">nevada</a></li>
<li><a href="/esit/nevado">nevado</a></li>
<li><a href="/esit/nevar">nevar</a></li>
<li><a href="/esit/nevera">nevera</a></li>
<li><a href="/esit/nevisca">nevisca</a></li>
<li><a href="/esit/nexo">nexo</a></li>
<li><a href="/esit/ni">ni</a></li>
<li><a href="/esit/nica">nica</a></li>
<li><a href="/esit/Nicaragua">Nicaragua</a></li>
<li><a href="/esit/nicarag%C3%BCense">nicaragüense</a></li>
<li><a href="/esit/nicho">nicho</a></li>
<li><a href="/esit/nicotina">nicotina</a></li>
<li><a href="/esit/nido">nido</a></li>
</ul></li>
</ul>

            
<ul>
    <li class="title1" title="Recent searches:">Búsquedas recientes:</li>
</ul>

<ul>
        <li id="wrsave"></li>
        <li style="list-style-type:none;" id="viewallhistory">
            <a href="/docs/searchHistory.aspx?dict=esit" target="_blank">Mostra tutti</a>
            <script>
                if ('localStorage' in window && window['localStorage'] !== null) {
                    if ((localStorage["bWRsaveHistory"]) && (localStorage["bWRsaveHistory"] == "false")) {
                        document.getElementById("viewallhistory").style.display = "none";
                    };
                }
            </script>
        </li>
</ul>

        </li>
    </ul>
</td>


                    
                    <td id="centercolumn">
                        
<div id="articleHead">

        

                    <h1 class="headerWord">nevar</h1>
                
            <div id="footerlink"><a href="#footer">[links]</a></div>
                
<div id='listen_widget'><span id='listen_txt' style='display: none;'>Escuchar:</span><input type='hidden' id='audT' value='3' /><script>var audioFiles = ['/audio/es/Mexico/es135620.mp3','/audio/es/Castellano/es135620.mp3','/audio/es/Argentina/es135620.mp3',];</script><span id='audiodrop'><select id='accentSelection'></select></span></div>
<script>
//Select Audio in local storage
var audPref = localStorage['wr_audio-'+strDic.substr(0,2)];
//Clear the cached selection
var sel = document.getElementById('accentSelection')
var audChoice = '<optgroup label="Accents"><option title="México pronunciation" value="0" >México</option><option title="Spain pronunciation" value="1" >España</option><option title="Argentina pronunciation" value="2" >Argentina</option></optgroup><optgroup label="Playback rate"><option title="Speed at 100%" value="%100">100%</option><option title="Speed at 75%" value="%75">75%</option><option title="Speed at 50%" value="%50">50%</option></optgroup>';
audChoice = audChoice.replace(/ selected=["']selected["']/gm, '');var audT = document.getElementById('audT');if ((audT) && (audPref)) {
		//Parse the content
		if(audPref.indexOf(':') > -1) {
			var audPrefAccent = audPref.split(':')[0];
			var playbackRate = audPref.split(':')[1];
		} else {
			var audPrefAccent = audPref;
			var playbackRate = 1;
		}
		var re = new RegExp('(<option[^>]+)(>' + audPrefAccent + '<\\/option>)','gm');		audChoice = audChoice.replace(re, "$1 selected='selected'$2");
}
sel.innerHTML = audChoice;
var isIE11 = (!!window.MSInputMethodContext && !!document.documentMode)
document.getElementById('listen_txt').style.display = 'inline';
if(isIE11)
	document.getElementById('listen_widget').style.display = 'none';
</script>
<div id='dummyspan'></div><br /> 


            <div id="forumNotes"><a id="forumNotesLink">ⓘ Una o más entradas de foro concuerdan exactamente con el término buscado</a></div>
            

<div id="WHlinks" style="padding-top: 8px;"> 
    <a href='/definicion/nevar'>definición</a> | 
<a href='/sinonimos/nevar'>sinónimos</a> | 
<a href='/gramatica/nevar'>Gramática </a> | 
<a href='/es/en/translation.asp?spen=nevar'>en inglés</a> | 
<a title='conjugación de verbos en español' rel='nofollow' href='/conj/esverbs.aspx?v=nevar'>Conjugación&nbsp;<span style='font-size:smaller'>[ES]</span></a> | 
<a title='conjugación de verbos en italiano' rel='nofollow' href='/conj/itverbs.aspx'>Coniugatore&nbsp;<span style='font-size:smaller'>[IT]</span></a> | 
<a title='in Context' Target='gg' href='https://www.google.es/search?tbm=nws&amp;lr=lang_es&amp;q=%22nevar%22'>en contexto</a> | 
<a title='images' Target='gg' href='https://www.google.es/search?tbm=isch&amp;safe=active&amp;q=%22nevar%22'>imágenes</a>

</div>

            <span id='strAnchors'></span>

        <br>
        


        <div class="hw-flex-container" style="direction: ltr">
            <div class="inflectionsSection">
                

        
    
                



                            
                                        

            </div><!-- End of inflectionsSection -->
        </div><!-- End of flex-container -->        
</div><!-- End of articleHead -->

                        

                            
<!-- articleWRD -->
                            <div id='articleWRD'></div><div id='collinsdiv'></div>
                            

                            

<div id="article">
        <div id='otherDicts'>
        


<br><div class='small1'>Compact Plus Italiano © HarperCollins Publishers 2007:</div><br>                            <style type='text/css' scoped='scoped'>
                                div#article {
                                    padding: 0px;
                                }

                                .entry {
                                    padding-bottom: 2em;
                                }

                                .pos {
                                    font-variant: small-caps;
                                }

                                .infl, div#article .alt, .drv, .phrase, .compound, .expanded, .xr, .opt {
                                    font-weight: bold;
                                }

                                .tran .pos {
                                    font-variant: normal;
                                    font-style: italic;
                                }

                                .tran .infl {
                                    font-weight: normal;
                                }

                                .gramcat {
                                    display: block;
                                    margin: 10px 0px 10px 10px
                                }

                                .phrasegroup, .compoundgroup {
                                    display: block;
                                    margin-left: 20px;
                                    padding-bottom: 0.2em
                                }

                                .cmpdmarker {
                                    margin-right: 3px;
                                    position: relative;
                                    top: -0.1em
                                }

                                li .phrasegroup {
                                    margin-left: 0px;
                                    padding-bottom: 0px
                                }

                                ol.senses {
                                    margin-top: 0.5em;
                                }

                                .inflgroup .alt {
                                    font-style: italic;
                                    font-weight: normal
                                }

                                /*.hwblk .inflgroup {
                                    font-style: italic;
                                }*/

                                .etc, .lbmisc, .ital, .subjarea, .lbgram, .groupintro {
                                    font-style: italic;
                                }

                                .tran.gloss {
                                    font-style: italic;
                                }

                                .expanded.ital, .or {
                                    font-weight: normal;
                                    font-style: italic
                                }

                                .infoblock {
                                    display: block;
                                    border: solid 1px #d1d1e5;
                                    border-radius: 3px;
                                    margin: 15px 25px 10px 0px;
                                    padding: 8px;
                                    background-color: #ebebff
                                }

                                .prongrp {
                                    padding-left: 3px;
                                }

                                q {
                                    quotes: "„" "“";
                                }
                            </style>

<div class='superentry collinsesitde trans clickable'><div  class='entry'><span class='hwblk'><strong class='hw'><hw>nevar</strong> <span class='prongrp'>[<span class='pron'>neˈβar</span>]</span></span> <span class='gramcat'><span class='pos'>vi</span><ol class='senses'><li class='sense' style='list-style-type:none'><span class='tran'>nevicare</span></li></ol></span></div></div>
            </div>
                <div class='virtual-article' style='padding: 0;'>
                    <!-- copyright 2 --><div><p class='wrcopyright'><a name="nevar110"></a><span dir='auto'>WordReference <span class='ph' data-ph='sLang_es'>Español</span>-<span class='ph' data-ph='sLang_it'>Italiano</span> Virtual Dictionary © 2024:</span></p><div id='virtualNote' class='notfound' style='display: none;'>Considere que se trata de un diccionario virtual, creado al combinar el diccionario Inglés=><span class='ph' data-ph='sLang_es'>Español</span> con el diccionario Inglés=><span class='ph' data-ph='sLang_it'>Italiano</span>. La calidad de los resultados puede no ser tan buena como la que verá en otros diccionarios de WordReference.</div></div><table class='WRD' data-dict='esit'><tr class='wrtopsection'><td colspan='3' title='Principal Translations'><strong><span class='ph' data-ph='sMainMeanings'>Traduzioni principali</span></strong></td></tr><tr class='langHeader' style='font-size: 13px;text-decoration: underline;font-weight:bold;'><td class='FrWrd'><span class='ph' data-ph='sLang_es'>Español</span></td><td></td><td class='ToWrd'><span class='ph' data-ph='sLang_it'>Italiano</span></td></tr>
<tr class='even' id='esit:13630'><td class='FrWrd'><span class='tooltip tooltipvirtual'><strong>nevar</strong><span>From the English "snow"</span></span> <em class='POS2' data-lang='es' data-abbr='v+impers'>v impers</em></td><td></td><td class='ToWrd' >nevicare<a title="conjugate nevicare" class='conjugate' href="/conj/itverbs.aspx?v=nevicare">⇒</a> <em class='POS2' data-lang='it' data-abbr='vi'>vi</em></td></tr>
<tr class='even'><td>&nbsp;</td><td colspan='2' class='FrEx'><span dir='ltr'>¿Ya está nevando?</span></td></tr>
<tr class='even'><td>&nbsp;</td><td colspan='2' class='ToEx' dir='ltr'>Sta ancora nevicando fuori?</td></tr>
</table>

                </div>
                    <script>
                        var hideSelectors = document.querySelectorAll('#noEntryFound, #spellSug, #articleHead p a[rel="nofollow"]');
                        for (var i = 0; i < hideSelectors.length; i++) {
                            hideSelectors[i].style.display = 'none';
                        }
                    </script>
                    

<div id='FTintro'><span class='ph' data-ph='sFTintro:nevar'>'<b>nevar</b>' aparece también en las siguientes entradas:</span>
</div>
<div class='FTlist'>
<a href="/esit/nieve">nieve</a>
</div>


</div> 
                            
<div id="postArticle">
    




    
<br><p id='threadsHeader' title='Forum discussions with the word(s) "nevar" in the title'><span class='ph' data-ph='sFDisc:nevar'>Preguntas en los foros con la(s) palabra(s) 'nevar' en el título:</span></p><div id="lista_link"><span style='font-style: italic;'><span class='ph' data-ph='langForumNoDiscussions:nevar|Italiano-Español'>No aparecen discusiones con "nevar" en el foro Italiano-Español.</span></span><br><br><a href='https://forum.wordreference.com/threads/est%C3%A1-para-nevar.1341459/'>est&#225; para nevar</a> - Spanish Only forum<br>
<a href='https://forum.wordreference.com/threads/nevar-a-saco.2091944/'>nevar a saco</a> - Spanish Only forum<br>
<a href='https://forum.wordreference.com/threads/nevar-o-nievar.1697019/'>nevar o nievar?</a> - Spanish Only forum<br>
<div class='extra_links'><a href='https://forum.wordreference.com/forums/53/' title="Visit the Italiano-Español Forum"><span class='ph' data-ph='sVisitForum:Italiano-Español|53'>Visita el foro Italiano-Español.</span></a><br /><a href='https://forum.wordreference.com/forums/53/' title="Ask in the forums yourself">Ayuda a WordReference: <span class='ph' data-ph='sAskYourself'>Pregunta tú mismo.</span></a></div></div> <!-- End lista_link -->



    

    <style>

        ul#announcement, ul#announcement a { 
            font-size: 12px; 
        }
        ul#announcement {
            margin: 0;
            border-top: 1px solid var(--announcement-border-color);
            margin-top: 2vh;
            margin-bottom: 2vh;
            border-radius: 10px;
            padding: 10px !important;
            background-color: var(--announcement-background-color);
        }
        ul#announcement > li {
            line-height: 20px;
            list-style: none;
            text-indent: -22px;
            padding-left: 22px;
        }
        html[dir=rtl] ul#announcement > li {
            text-indent: 0;
        }
        .annIcon {
            display: inline-block;
            background: url(/images/announcement.svg) no-repeat left center;
            width: 20px;
            height: 16px;
            line-height: 20px;
            vertical-align: text-bottom;
        }
        html[dir=rtl] .annIcon {
            -moz-transform: scaleX(-1);
            -o-transform: scaleX(-1);
            -webkit-transform: scaleX(-1);
            transform: scaleX(-1);
            filter: FlipH;
            -ms-filter: "FlipH";
        }
        @media screen and (max-width: 769px) {
            ul#announcement {
                padding: 5px 10px 5px 10px;
                border-bottom: none;
            }
        }
    </style>
    <ul id="announcement">
            <li><span class="annIcon"></span><span>Go to <a href='/preferences'>Preferences</a> page and choose from different actions for taps or mouse clicks.</span></li>
    </ul>


        

                <span style="border: 0 none;" id="gtrans" dir="auto"><a href="#" rel="nofollow" title="See Google Translate's machine translation of 'nevar'." onclick="iframeGGapi(); return false">Vedi la traduzione automatica di Google Translate di "nevar".</a><br></span>
                <script>
                    function iframeGGapi() {
                        var sOriginal = 'nevar';
                        var DestLang = "it";
                        var SourceLang = "es";
                        document.getElementById('gtrans').innerHTML = "<iframe style='border: 0 none;' src='/dictionary/googTranslate?dict=" + SourceLang + DestLang + "&w=" + sOriginal + "&sk=t' width='100%' height='55'><\\/iframe>";
                    }
                </script>

            <p class='other_languages'><span title='In other languages:'>En otros idiomas:</span> <a href='/esfr/nevar'  title='French'>Francés</a> | <a href='/espt/nevar'  title='Portuguese'>Portugués</a> | <a href='/esde/nevar'  title='German'>Alemán</a> | <a href='/esnl/nevar' rel='nofollow' title='Dutch'>Holandés</a> | <a href='/essv/nevar' rel='nofollow' title='Swedish'>Sueco</a> | <a href='/espl/nevar' rel='nofollow' title='Polish'>Polaco</a> | <a href='/esro/nevar' rel='nofollow' title='Romanian'>Rumano</a> | <a href='/escz/nevar' rel='nofollow' title='Czech'>Checo</a> | <a href='/esgr/nevar' rel='nofollow' title='Greek'>Griego</a> | <a href='/estr/nevar' rel='nofollow' title='Turkish'>Turco</a> | <a href='/eszh/nevar' rel='nofollow' title='Chinese'>Chino</a> | <a href='/esja/nevar' rel='nofollow' title='Japanese'>Japonés</a> | <a href='/esko/nevar' rel='nofollow' title='Korean'>Coreano</a> | <a href='/esar/nevar' rel='nofollow' title='Arabic'>Árabe</a> | <a href='/esen/nevar'  title='English'>Inglés</a> </p>
        

        

    <div id="postLinks">
        <span title="Links">Enlaces:</span>
        <a href='/Preferences'>⚙️Preferencias</a> | 
<a title='Privacy Policy' href='/english/Privacy%20Policy.htm'>Regole sulla privacy</a> | 
<a title='Terms of Service' href='/english/TermsOfService.aspx'>Términos del Servicio</a> | 
<a title='Support WR' href='/docs/support-wordreference.aspx'>Apoyar WR</a> | 
<a title='Forums' href='https://forum.wordreference.com/'>Foros</a> | 
<a title='Suggestions' href='https://forum.wordreference.com/misc/contact'>Sugerencias</a>

    </div>

</div> <!-- End of postArticle -->

<!-- Other scripts-->


                        

                    </td>
                    

                    
    <td id="rightcolumn">
        <table class="rightcolumn">
            <tbody>
                
            <tr class='adtitle' style='width:100%'><td colspan='2' style='text-align:center;color:gray;'>Publicidad</td></tr>
            <tr style='width:100%'>
                <td colspan='2' style='height:260px;border-bottom: solid 1px #dcdcdc;padding-bottom:5px'>

                                <!-- adngin-side_mpu_1-0 -->
                                <div id="adngin-side_mpu_1-0"></div>
                                            </td>
            </tr>
            <tr class='adtitle' style='width:100%'><td colspan='2' style='text-align: center;color: gray;'>Publicidad</td></tr>
            <tr style='width: 100%;'>
                <td colspan='2' style='height:260px;width: 100%; border-bottom: solid 1px #dcdcdc; padding-bottom: 5px;'>

                                <!-- adngin-side_mpu_2-0 -->
                                <div id="adngin-side_mpu_2-0"></div>
                                            </td>
            </tr>
            <tr style='width:100%'>
                <td colspan='2' style='padding: 5px 0 7px 0;border-bottom: solid 1px #dcdcdc;'>
                    <a href="/docs/report.ad.aspx?dict=esit" target="_blank" title="Report an inappropriate ad." style="font-size:12px;text-align:left;margin-left:5px;">Infórmanos de los anuncios inapropiados.</a>
                </td>
            </tr>
    <tr id='wotdTR' style='height: 35px; width:100%; display: table-row;'>
        <td colspan='2' style='text-align:center;border-bottom:solid 1px #dcdcdc;border-collapse:collapse'>
            <div class='wotd'>
                <span style="position: absolute !important;text-align: left;display: inline-block;left: 52px;font-size: 11px;">
                    WordReference.com
                </span>
                <div id='wotdTitle'>WORD OF THE DAY</div>
                <div id='wotdContent' style='min-height: 38px;padding: 8px 0 8px 0;'>
                    <script async src="/dictionary/wotdscript"></script>
                </div>   
                <div id='wotdSubscribe'>
                    <div id="wotdSubtitle">GET THE DAILY EMAIL!</div>
                    <input class="subscribeBtn" type="button" value="Subscribe!" onclick="window.location.href='https://daily.wordreference.com'" />
                </div>
            </div>
        </td>
    </tr>
        <tr style='width:100%;'>
            <td colspan='2' style='text-align:center;border-bottom:solid 1px #dcdcdc;border-collapse:collapse'>
                <p style='margin-right:-2px'>
                <a id='GooglePlay' href='https://play.google.com/store/apps/details?id=com.wordreference' title='Android App' style='background-position:-5px -61px;background-repeat:no-repeat;'></a>
                <a href='https://apps.apple.com/us/app/wordreference-dictionary/id515127233' id='AppStore' title='iPhone App' style='background-position:-5px -5px;background-repeat:no-repeat;'></a>
            </td>
        </tr>
    <tr style='width:100%'>
        <td colspan='2' class='wrSupportRightAdLink' style='border-collapse:collapse;font-size:12px;text-align:left;padding-left:5px;padding-top:6px'>
            <a href="/docs/supporter.aspx" target="_blank" title="WordReference Supporter - no ads">Conviértete en un Patrocinador de WordReference para ver este sitio sin anuncios.</a>
        </td>
    </tr>
        <tr>
            <td colspan="2">
                <div dir="auto" class="FCboxes" title="Scorciatoia per Chrome"> 
                    <b class="highlight">Utenti Chrome:</b> usate le <a href="/tools/Chrome-search-shortcut.aspx">scorciatoie di ricerca</a> per una ricerca più veloce su WordReference.
                </div>
            </td>
        </tr>

            </tbody>
        </table>
    </td>

                </tr>
            </table>
        </div>
        
    


<div id="footer">

    


<table class='footer'>
    <tr>
        <td><a href="/english/copyright.aspx">Copyright / derecho de autor</a> © 2024 WordReference.com</td>
        <td style="display: flex; align-items: end; justify-content: flex-end;">
            <div id="eplinkContainer">
                <a id='englishPageLink' href='javascript:;'><span><svg xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink' aria-hidden='true' focusable='false' width='14px' height='14px' style='-ms-transform: rotate(360deg); -webkit-transform: rotate(360deg); transform: rotate(360deg);' preserveAspectRatio='xMidYMid meet' viewBox='0 0 1536 1792'><path d='M654 1078q-1 3-12.5-.5T610 1066l-20-9q-44-20-87-49q-7-5-41-31.5T424 948q-67 103-134 181q-81 95-105 110q-4 2-19.5 4t-18.5 0q6-4 82-92q21-24 85.5-115T393 918q17-30 51-98.5t36-77.5q-8-1-110 33q-8 2-27.5 7.5T308 792t-17 5q-2 2-2 10.5t-1 9.5q-5 10-31 15q-23 7-47 0q-18-4-28-21q-4-6-5-23q6-2 24.5-5t29.5-6q58-16 105-32q100-35 102-35q10-2 43-19.5t44-21.5q9-3 21.5-8t14.5-5.5t6 .5q2 12-1 33q0 2-12.5 27T527 769.5T510 803q-25 50-77 131l64 28q12 6 74.5 32t67.5 28q4 1 10.5 25.5t4.5 30.5zM449 592q3 15-4 28q-12 23-50 38q-30 12-60 12q-26-3-49-26q-14-15-18-41l1-3q3 3 19.5 5t26.5 0t58-16q36-12 55-14q17 0 21 17zm698 129l63 227l-139-42zM39 1521l694-232V257L39 490v1031zm1241-317l102 31l-181-657l-100-31l-216 536l102 31l45-110l211 65zM777 242l573 184V46zm311 1323l158 13l-54 160l-40-66q-130 83-276 108q-58 12-91 12h-84q-79 0-199.5-39T318 1668q-8-7-8-16q0-8 5-13.5t13-5.5q4 0 18 7.5t30.5 16.5t20.5 11q73 37 159.5 61.5T714 1754q95 0 167-14.5t157-50.5q15-7 30.5-15.5t34-19t28.5-16.5zm448-1079v1079l-774-246q-14 6-375 127.5T19 1568q-13 0-18-13q0-1-1-3V474q3-9 4-10q5-6 20-11q107-36 149-50V19l558 198q2 0 160.5-55t316-108.5T1369 0q20 0 20 21v418z' fill='#626262'/><rect x='0' y='0' width='1536' height='1792' fill='rgba(0, 0, 0, 0)' /></svg></span>English version</a>
            </div>
            <div style="text-align:right;white-space: nowrap;" title="Please report any problems.">Por favor, <a href="https://forum.wordreference.com/misc/contact">comunícanos</a> cualquier problema</div>
        </td>
    </tr>
</table>

</div>


    </div>
    





<script>
	//for placeholder text to fade on focus
	if (document.getElementById("si")){
		document.getElementById("si").onfocus = function(){
			document.getElementById("si").placeholder = '';
		};
	}
</script>

<!--[if lt IE 9]>
<script>
	if (document.getElementById("listen_widget")){
		function addUpgradeNotice(){
			if (!document.getElementById("audtag")){
				if (!document.getElementById("ieupgrade")){
					var upgradeDiv = document.createElement("div");
					upgradeDiv.id = 'ieupgrade';
					upgradeDiv.innerHTML = 'The audio on WordReference works best with the latest version of Internet Explorer. <a target="_blank" href="http://windows.microsoft.com/en-US/internet-explorer/downloads/ie/">Upgrade now!</a>';
					document.getElementById("listen_widget").parentElement.insertBefore(upgradeDiv, document.getElementById("listen_widget").nextSibling);
				}
			}
		}
	
		document.getElementById("listen_widget").onclick = function(){
			return addUpgradeNotice();
		}
		function dismissUpgrade(){
			document.getElementById("ieupgrade").parentElement.removeChild(document.getElementById("ieupgrade"));
		}

	}
</script>
<![endif]-->





<script>
    var dMatch = true;
    var fMatch = false;
    var isReverseDict = false;
    var isVirtualDict = false;

    var visitor = {
        browser: 0,
        browserOS: 1,
        browserVersion: 0,
        platform: 0,
        country: "US"
    };

    gtag('event', 'www', {
      'event_category': 'site',
      'non_interaction': true
    });

    gtag('event', 'wwwor1-44b5556a', {
        'non_interaction': true,
        'event_callback': function() {
            consoleDebug('wwwor1-44b5556a');
        }
    });

    //ga('send', { hitType: 'event', eventCategory: '', eventAction: 'www'}, {nonInteraction: true});
    /*
    if (typeof GDPRcookieYes !== "undefined") {
        ga('send', 'GDPRcookieYes', {
        'dimension3':   GDPRcookieYes.toString()
        });
    }
    */

</script>

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "BreadcrumbList",
    "itemListElement": [{
    "@type": "ListItem",
    "position": 1,
    "item": {
        "@id": "//www.wordreference.com/esit/",
        "name": "Dictionaries"
    }
    },{
        "@type": "ListItem",
        "position": 2,
        "item": {
        "@id": "//www.wordreference.com/esit/nevar",
        "name": "nevar"
        }
    }]
}
</script>



    <script type="text/javascript" src="/js/swInstall.min.js?v=Rq10VgPmYxBIuFlB1JonizGyxUJmVFc1nWl5ldHRt9w"></script>

<script>
    console.log(">> Server name:", 'wwwor1');
</script>
    <script> 
</script>
</body>
</html>
"""
