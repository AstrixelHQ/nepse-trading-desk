# StockYan Research (नेपाली)

Claude, ChatGPT, Gemini जस्ता AI मा NEPSE शेयरको रिसर्च एक जना अनुभवी analyst ले जस्तै गर्न सिकाउने खुला
(open-source) skill। StockYan connector ले AI लाई live data दिन्छ: मूल्य, कम्पनीका वित्तीय विवरण, ब्रोकरको खरिद
बिक्री, technical र fundamental scanner, र तपाईंको आफ्नै portfolio।

> **यो रिसर्च हो, लगानी सल्लाह होइन।** यसले शेयर किन वा बेच भन्दैन, साँचो order राख्दैन, र देखाइएका सबै
> अंक StockYan को live data बाट मिति सहित आउँछन्।

## यसले के गर्छ

1. चार कोणबाट प्रमाण जम्मा गर्छ: fundamentals, technicals, broker flow र सन्दर्भ (sector, समाचार)।
2. पक्षमा तर्क (bull case) लेख्छ, अनि त्यसको सबैभन्दा बलियो बुँदाको विपक्षमा जवाफ (bear case) दिन्छ।
3. जोखिम हेर्छ: liquidity, १५% को दैनिक मूल्य सीमा, book closure, lock-in खुल्ने मिति।
4. निष्कर्ष सर्तसहित दिन्छ: प्रमाण कता ढल्किन्छ, कति बलियो, र कुन level वा मितिमा धारणा बदलिन्छ।

## कसरी जोड्ने

- **Claude Code:** `/plugin marketplace add AstrixelHQ/stockyan-skills` अनि `/plugin install stockyan-research@stockyan`
- **Claude (web, app):** connector `https://stockyan.astrixel.com/mcp` थप्नुहोस्, अनि Releases बाट
  `stockyan-research.zip` डाउनलोड गरेर Customize → Skills → Upload a skill।
- **Gemini CLI:** `gemini extensions install https://github.com/AstrixelHQ/stockyan-skills`
- **अन्य AI:** `npx skills add AstrixelHQ/stockyan-skills`

## सोध्ने उदाहरण

```
NABIL अहिले किन्न लायक छ?
सस्तो र ब्रोकरले किनिरहेका ३ वटा hydropower शेयर देखाऊ।
मेरो portfolio हेरिदेऊ।
NEPSE aaja kasto bhayo?
```

पूरा अंग्रेजी विवरण: [README.md](README.md)
