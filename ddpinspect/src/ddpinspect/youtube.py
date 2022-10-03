"""
DDP Youtube module

This module contains functions to handle files contained within an youtube ddp
"""

from typing import Any
import logging

import pandas as pd

from ddpinspect import scanfiles

logger = logging.getLogger(__name__)


def watch_history_to_df(watch_history: list[dict[Any, Any]]) -> pd.DataFrame | None:
    """
    Converts list[dict[Any, Any]] obtained from watch-history.json to pd.DataFrame
    """

    df_out = None

    try:
        if not isinstance(watch_history, (dict, list)):
            raise TypeError("Incorrect input type expected dict or list")

        df_out = pd.DataFrame([scanfiles.dict_denester(item) for item in watch_history])

    except TypeError as e:
        logger.error(e)
    except Exception as e:
        logger.error("Exception was caught:  %s", e)

    finally:
        return df_out
