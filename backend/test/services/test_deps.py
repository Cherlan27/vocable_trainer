from src.services.deps import get_llm_service, get_voc_generator


def test_get_llm_service():
    llm_service = get_llm_service()
    assert llm_service is not None
    assert hasattr(llm_service, "url")


def test_get_voc_generator():
    voc_generator = get_voc_generator()
    assert voc_generator is not None
    assert hasattr(voc_generator, "llm")
