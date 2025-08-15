---
title: Example 1: Scrape a webpage as Markdown
category: misc
source_lines: 79247-79343
line_count: 96
---

# Example 1: Scrape a webpage as Markdown
agent.print_response(
    "Scrape this webpage as markdown: https://docs.agno.com/introduction",
)
```

## Toolkit Parameters

These parameters are passed to the `BrightDataTools` constructor.

| Parameter            | Type            | Default           | Description                                                                                                  |
| -------------------- | --------------- | ----------------- | ------------------------------------------------------------------------------------------------------------ |
| `api_key`            | `Optional[str]` | `None`            | BrightData API key. If not provided, uses `BRIGHT_DATA_API_KEY` environment variable.                        |
| `serp_zone`          | `str`           | `"serp_api"`      | Zone for search engine requests. Can be overridden with `BRIGHT_DATA_SERP_ZONE` environment variable.        |
| `web_unlocker_zone`  | `str`           | `"web_unlocker1"` | Zone for web scraping requests. Can be overridden with `BRIGHT_DATA_WEB_UNLOCKER_ZONE` environment variable. |
| `scrape_as_markdown` | `bool`          | `True`            | Enable the `scrape_as_markdown` tool.                                                                        |
| `get_screenshot`     | `bool`          | `False`           | Enable the `get_screenshot` tool.                                                                            |
| `search_engine`      | `bool`          | `True`            | Enable the `search_engine` tool.                                                                             |
| `web_data_feed`      | `bool`          | `True`            | Enable the `web_data_feed` tool.                                                                             |
| `verbose`            | `bool`          | `False`           | Enable verbose logging.                                                                                      |
| `timeout`            | `int`           | `600`             | Timeout in seconds for web data feed requests.                                                               |

## Toolkit Functions

| Function             | Description                                                                                                                                                                                                                           |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `scrape_as_markdown` | Scrapes a webpage and returns content in Markdown format. Parameters: `url` (str) - URL to scrape.                                                                                                                                    |
| `get_screenshot`     | Captures a screenshot of a webpage and adds it as an image artifact. Parameters: `url` (str) - URL to screenshot, `output_path` (str, optional) - Output path (default: "screenshot.png").                                            |
| `search_engine`      | Searches using Google, Bing, or Yandex and returns results in Markdown. Parameters: `query` (str), `engine` (str, default: "google"), `num_results` (int, default: 10), `language` (Optional\[str]), `country_code` (Optional\[str]). |
| `web_data_feed`      | Retrieves structured data from various sources like LinkedIn, Amazon, Instagram, etc. Parameters: `source_type` (str), `url` (str), `num_of_reviews` (Optional\[int]).                                                                |

## Supported Data Sources

The `web_data_feed` function supports the following source types:

### E-commerce

* `amazon_product` - Amazon product details
* `amazon_product_reviews` - Amazon product reviews
* `amazon_product_search` - Amazon product search results
* `walmart_product` - Walmart product details
* `walmart_seller` - Walmart seller information
* `ebay_product` - eBay product details
* `homedepot_products` - Home Depot products
* `zara_products` - Zara products
* `etsy_products` - Etsy products
* `bestbuy_products` - Best Buy products

### Professional Networks

* `linkedin_person_profile` - LinkedIn person profiles
* `linkedin_company_profile` - LinkedIn company profiles
* `linkedin_job_listings` - LinkedIn job listings
* `linkedin_posts` - LinkedIn posts
* `linkedin_people_search` - LinkedIn people search results

### Social Media

* `instagram_profiles` - Instagram profiles
* `instagram_posts` - Instagram posts
* `instagram_reels` - Instagram reels
* `instagram_comments` - Instagram comments
* `facebook_posts` - Facebook posts
* `facebook_marketplace_listings` - Facebook Marketplace listings
* `facebook_company_reviews` - Facebook company reviews
* `facebook_events` - Facebook events
* `tiktok_profiles` - TikTok profiles
* `tiktok_posts` - TikTok posts
* `tiktok_shop` - TikTok shop
* `tiktok_comments` - TikTok comments
* `x_posts` - X (Twitter) posts

### Other Platforms

* `google_maps_reviews` - Google Maps reviews
* `google_shopping` - Google Shopping results
* `google_play_store` - Google Play Store apps
* `apple_app_store` - Apple App Store apps
* `youtube_profiles` - YouTube profiles
* `youtube_videos` - YouTube videos
* `youtube_comments` - YouTube comments
* `reddit_posts` - Reddit posts
* `zillow_properties_listing` - Zillow property listings
* `booking_hotel_listings` - Booking.com hotel listings
* `crunchbase_company` - Crunchbase company data
* `zoominfo_company_profile` - ZoomInfo company profiles
* `reuter_news` - Reuters news
* `github_repository_file` - GitHub repository files
* `yahoo_finance_business` - Yahoo Finance business data

## Developer Resources

* View [Tools Source](https://github.com/agno-agi/agno/blob/main/libs/agno/agno/tools/brightdata.py)
* View [Cookbook Example](https://github.com/agno-agi/agno/blob/main/cookbook/tools/brightdata_tools.py)


