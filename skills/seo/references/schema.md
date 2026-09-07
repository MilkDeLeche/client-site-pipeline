# Schema markup (JSON-LD)

Structured data tells search engines and language models what a page *is*, rather than making them infer it. It earns rich results in Google and makes facts cleanly extractable for AI answers.

## Rules

- **JSON-LD only**, in a `<script type="application/ld+json">`. Microdata and RDFa are legacy.
- **Never mark up what isn't on the page.** Invented ratings or fabricated prices are a manual-action risk, and for reviews a legal one.
- **Absolute URLs.** ISO 8601 dates.
- **Omit optional fields you can't fill** — never leave empty strings.
- **Use the most specific type available.** `Restaurant` beats `LocalBusiness` beats `Organization`.
- **Validate** at [validator.schema.org](https://validator.schema.org) for correctness and Google's [Rich Results Test](https://search.google.com/test/rich-results) for eligibility. They answer different questions.
- Multiple types per page is normal — link them with `@id` rather than repeating blocks.

---

## LocalBusiness — the important one

For any business with a location. Use the most specific subtype: `Restaurant`, `CafeOrCoffeeShop`, `Bakery`, `HealthAndBeautyBusiness`, `Store`.

```json
{
  "@context": "https://schema.org",
  "@type": "Restaurant",
  "@id": "https://example.com/#business",
  "name": "Feel Good",
  "url": "https://example.com",
  "logo": "https://example.com/logo.png",
  "image": ["https://example.com/storefront.jpg"],
  "description": "Cold-pressed juice, açaí bowls and waffles in Brownsville, Texas. Plant-based, gluten-free, refined-sugar-free.",
  "telephone": "+1-956-667-5300",
  "priceRange": "$$",
  "servesCuisine": ["Juice", "Açaí", "Vegan"],
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "800 N. Expressway 77/83, Suite 17",
    "addressLocality": "Brownsville",
    "addressRegion": "TX",
    "postalCode": "78521",
    "addressCountry": "US"
  },
  "geo": {
    "@type": "GeoCoordinates",
    "latitude": 25.9,
    "longitude": -97.5
  },
  "openingHoursSpecification": [
    {
      "@type": "OpeningHoursSpecification",
      "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
      "opens": "10:00",
      "closes": "18:00"
    },
    {
      "@type": "OpeningHoursSpecification",
      "dayOfWeek": "Saturday",
      "opens": "10:00",
      "closes": "14:00"
    }
  ],
  "sameAs": [
    "https://www.instagram.com/feelgood.tx/",
    "https://www.facebook.com/..."
  ],
  "hasMenu": "https://example.com/menu",
  "acceptsReservations": "False"
}
```

`geo` coordinates should come from the actual Google Business Profile pin, not a geocoder guess at the street address — for a suite in a strip mall those differ.

`sameAs` is how you tell Google that this website, this Instagram and this Facebook page are one entity. It matters for the knowledge panel and for AI confidence.

## Menu

```json
{
  "@context": "https://schema.org",
  "@type": "Menu",
  "@id": "https://example.com/menu#menu",
  "hasMenuSection": [
    {
      "@type": "MenuSection",
      "name": "Cold-Pressed Juices",
      "hasMenuItem": [
        {
          "@type": "MenuItem",
          "name": "Green Press",
          "description": "Kale, cucumber, green apple, lemon, ginger.",
          "offers": { "@type": "Offer", "price": "9.00", "priceCurrency": "USD" },
          "suitableForDiet": ["https://schema.org/VeganDiet", "https://schema.org/GlutenFreeDiet"]
        }
      ]
    }
  ]
}
```

`suitableForDiet` is the field that surfaces a business in dietary-filtered searches. For a vegan/GF business it's one of the highest-value properties available and almost nobody uses it.

## Organization

Homepage, for any business.

```json
{
  "@context": "https://schema.org",
  "@type": "Organization",
  "@id": "https://example.com/#org",
  "name": "",
  "url": "https://example.com",
  "logo": "https://example.com/logo.png",
  "description": "",
  "sameAs": [],
  "contactPoint": {
    "@type": "ContactPoint",
    "telephone": "+1-",
    "contactType": "customer service"
  }
}
```

## Article / BlogPosting

```json
{
  "@context": "https://schema.org",
  "@type": "BlogPosting",
  "headline": "",
  "description": "",
  "image": "",
  "author": { "@type": "Person", "name": "", "url": "" },
  "publisher": { "@id": "https://example.com/#org" },
  "datePublished": "2026-08-12",
  "dateModified": "2026-08-12",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "" }
}
```

`headline` is capped at 110 characters. A real `author` with a bio page is an E-E-A-T signal and an AEO signal.

## FAQPage

The highest-yield schema for AI citation. Answers self-contained, 40–60 words.

```json
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Is everything on the menu vegan?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes. Every item is plant-based, dairy-free, gluten-free, and made without refined sugar or refined flour."
      }
    }
  ]
}
```

The Q&A must be visible on the page. Schema-only FAQ is a violation. Note that Google now shows FAQ rich results only for authoritative health and government sites — but the schema still helps AI extraction, which is the reason to keep using it.

## HowTo, Product, BreadcrumbList

```json
{
  "@context": "https://schema.org",
  "@type": "HowTo",
  "name": "",
  "step": [{ "@type": "HowToStep", "name": "", "text": "" }]
}
```

```json
{
  "@context": "https://schema.org",
  "@type": "Product",
  "name": "",
  "image": "",
  "brand": { "@type": "Brand", "name": "" },
  "offers": {
    "@type": "Offer",
    "price": "",
    "priceCurrency": "USD",
    "availability": "https://schema.org/InStock"
  }
}
```

`aggregateRating` on a Product only if the ratings are real and shown on the page.

```json
{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    { "@type": "ListItem", "position": 1, "name": "Home", "item": "https://example.com" },
    { "@type": "ListItem", "position": 2, "name": "Menu", "item": "https://example.com/menu" }
  ]
}
```

---

## Astro

Site-wide schema goes in the layout; per-page schema in the page.

```astro
---
const schema = { "@context": "https://schema.org", "@type": "Restaurant", /* … */ };
---
<script type="application/ld+json" set:html={JSON.stringify(schema)} />
```

`set:html` with `JSON.stringify` — not a template literal, which will break on any apostrophe in the data. Build the object from the single business-facts data file so schema and visible page content can never disagree.
