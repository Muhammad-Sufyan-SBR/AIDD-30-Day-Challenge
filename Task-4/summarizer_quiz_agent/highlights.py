from datetime import datetime

def add_annotation(session_data, text_reference, note):
    """
    Adds a user annotation to the session data.
    """
    if "annotations" not in session_data:
        session_data["annotations"] = []
    
    annotation = {
        "id": len(session_data["annotations"]) + 1,
        "text_ref": text_reference,
        "note": note,
        "timestamp": datetime.now().isoformat()
    }
    session_data["annotations"].append(annotation)
    return session_data

def get_annotations(session_data):
    return session_data.get("annotations", [])
