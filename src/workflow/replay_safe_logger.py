class ReplaySafeLogger:
    """
    A logger that is safe to use in the workflow code to avoid
    duplicate logs when sections of the workflow are replayed.
    """
    def __init__(self, ctx, base_logger=None):
        self.ctx = ctx
        self.base_logger = base_logger

    def _should_log(self):
        return not self.ctx.is_replaying

    def info(self, msg, *args, **kwargs):
        if self._should_log():
            self.base_logger.info(msg, *args, **kwargs)

    def error(self, msg, *args, **kwargs):
        if self._should_log():
            self.base_logger.error(msg, *args, **kwargs)