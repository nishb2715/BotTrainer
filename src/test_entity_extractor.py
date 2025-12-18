from src.entity_extractor import extract_entities

text = "Book a flight to Delhi tomorrow"
intent = "book_flight"
entities_allowed = ["location", "date"]

entities = extract_entities(text, intent, entities_allowed)
print(entities)
