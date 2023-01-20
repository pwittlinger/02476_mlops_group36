import torch
from transformers import PegasusTokenizer, PegasusForConditionalGeneration
from tests import _PROJECT_ROOT
from os.path import exists

#import pytest


def test_model():
    """Parameters are set correctly
    Instatiated correctly"""
    _MODEL_PATH = "models/model.pt/"
    assert exists(_PROJECT_ROOT+"/"+_MODEL_PATH)
    tokenizer = PegasusTokenizer.from_pretrained(_MODEL_PATH)
    model = PegasusForConditionalGeneration.from_pretrained(_MODEL_PATH)
    device = 'cuda' if torch.cuda.is_available() else 'cpu'
    assert model.parameters