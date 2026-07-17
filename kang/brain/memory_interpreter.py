def interpret_memory(text, creator_name):
    interpreted_text = text

    if interpreted_text.starwith("Ben "):
        interpreted_text = creator_name + interpreted_text[3:]

    interpreted_text = interpreted_text.replace(
        "oyuncağım",
        creator_name + "'in oyuncağı"
    )

    interpreted_text = interpreted_text.replace(
        "çok seviyordum",
        "çok seviyordu"
    )

    return interpreted_text