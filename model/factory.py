from abc import ABC, abstractmethod
from typing import Optional

from langchain_community.embeddings import DashScopeEmbeddings
from langchain_community.chat_models import ChatTongyi
from langchain_core.language_models import BaseChatModel
from langchain_core.embeddings import Embeddings
from utils.config_handler import rag_config


# 创建父类
class BaseModelFactory(ABC):

    # 因为是抽象方法，所以不用写实际的代码
    @abstractmethod
    def generator(self) -> Optional[Embeddings | BaseChatModel]:
        pass


# chat子类
class ChatModelFactory(BaseModelFactory):

    def generator(self) -> Optional[Embeddings | BaseChatModel]:
        return ChatTongyi(model=rag_config["chat_model_name"])


class EmbeddingsFactory(BaseModelFactory):
    def generator(self) -> Optional[Embeddings | BaseChatModel]:
        return DashScopeEmbeddings(model=rag_config["embedding_model_name"])


# 实例化这两个子类，方便其他文件调用
chat_model = ChatModelFactory().generator()
embedding_model = EmbeddingsFactory().generator()