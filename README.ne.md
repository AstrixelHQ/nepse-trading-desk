# NEPSE Trading Desk (नेपाली)

नेप्सेका लागि AI रिसर्च डेस्क। Claude, ChatGPT, Gemini जस्ता AI मा StockYan को live data प्रयोग गरेर एउटा पेशेवर
टोलीले जस्तै काम गर्छ, र नयाँ लगानीकर्ताले पनि बुझ्ने गरी सजिलो भाषामा रिपोर्ट दिन्छ।

> **यो रिसर्च हो, लगानी सल्लाह होइन।** यसले शेयर किन वा बेच भन्दैन, साँचो order राख्दैन, र देखाइएका सबै
> अंक StockYan को live data बाट मिति सहित आउँछन्। Paper trade तपाईंले हुन्छ भनेपछि मात्र।

## डेस्कले के गर्छ (११ चरण)

1. **बजारको अवस्था:** NEPSE आफ्नो २०० दिने औसतभन्दा माथि छ कि तल? यसले कति लगानी गर्ने भन्ने तय गर्छ।
2. **धेरै रणनीति:** breakout, pullback, oversold, momentum, smart money, value। दुई रणनीतिले भेटेको शेयर अगाडि।
3. **विश्लेषक टोली:** fundamentals, technicals, broker flow र सन्दर्भ, हरेकलाई २५ अंक, जम्मा १०० को score।
4. **Smart money:** कुन ब्रोकरले हप्तौँदेखि किनिरहेको छ, कुल कारोबारको तुलनामा।
5. **पक्ष र विपक्ष:** किन काम गर्न सक्छ, किन असफल हुन सक्छ।
6. **ट्रेड योजना:** कहाँ किन्ने, कहाँ बाहिरिने (stop), लक्ष्य, र कति किन्ने। १५% को दैनिक सीमाले हुने जोखिम समेत।
7. **Portfolio:** एउटै sector मा ३०% भन्दा बढी नहोस्, कम्तीमा १५% नगद।
8. **जोखिम जाँच:** ११ वटा जाँच; खतरा भए रोक्छ।
9. **Paper trade:** तपाईंले हुन्छ भनेपछि मात्र, virtual पैसामा अभ्यास।
10. **Backtest:** यो रणनीतिले पहिले काम गरेको थियो कि थिएन?
11. **रिपोर्ट:** सजिलो भाषा, रंगीन संकेत (🟢🟡🔴), score bar र मूल्यको सिढी।

## कसरी जोड्ने

- **Claude, ChatGPT, Gemini app:** StockYan connector `https://stockyan.astrixel.com/mcp` थप्नुहोस्। बस, पूरा डेस्क
  त्यसैमा आउँछ। Claude मा: stockyan.com मा "Add to Claude" थिच्नुहोस्।
- **Claude Code:** `claude plugin install nepse-trading-desk --marketplace AstrixelHQ/nepse-trading-desk`
- **Gemini CLI:** `gemini extensions install https://github.com/AstrixelHQ/nepse-trading-desk`
- **अन्य AI:** `npx skills add AstrixelHQ/nepse-trading-desk`

## सोध्ने उदाहरण

```
यो हप्ता कुन शेयर हेर्ने?
NABIL अहिले किन्न लायक छ? २ लाखमा योजना बनाइदेऊ।
Oversold bank शेयर किन्दा पहिले फाइदा भएको थियो? Backtest गर।
मेरो portfolio हेरिदेऊ।
NEPSE aaja kasto bhayo?
```

पूरा अंग्रेजी विवरण: [README.md](README.md)
