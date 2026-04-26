#!/usr/bin/env python3
"""
Interface abstractions for integrated spec domain subsystems.

Provides:
- Canonical command/response payload models
- Core subsystem lifecycle base class
- Behavioral interfaces for commanding, monitoring, and observability
"""

from __future__ import annotations

import logging
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import Any


@dataclass(slots=True)
class SubsystemCommand:
    """Represents a command issued to a subsystem."""

    command_id: str
    command_type: str
    payload: dict[str, Any] = field(default_factory=dict)
    metadata: dict[str, Any] = field(default_factory=dict)


@dataclass(slots=True)
class SubsystemResponse:
    """Represents a subsystem command execution result."""

    command_id: str
    success: bool
    data: Any | None = None
    error: str | None = None
    execution_time_ms: float | None = None


class BaseSubsystem(ABC):
    """
    Minimal subsystem lifecycle base class.

    Subclasses should extend behavior while preserving lifecycle semantics.
    """

    def __init__(
        self,
        data_dir: str = "data",
        config: dict[str, Any] | None = None,
    ):
        self.data_dir = data_dir
        self.config = config or {}
        self._initialized = False
        self.logger = logging.getLogger(self.__class__.__name__)

    @abstractmethod
    def initialize(self) -> bool:
        """Initialize subsystem resources."""

    @abstractmethod
    def shutdown(self) -> bool:
        """Release subsystem resources and stop processing."""

    @abstractmethod
    def health_check(self) -> bool:
        """Return True when subsystem is healthy and operational."""

    def get_status(self) -> dict[str, Any]:
        """Return common status payload for subsystem diagnostics."""
        return {
            "subsystem": self.__class__.__name__,
            "initialized": self._initialized,
            "healthy": self.health_check(),
        }


class ICommandable(ABC):
    """Interface for command execution support."""

    @abstractmethod
    def execute_command(self, command: SubsystemCommand) -> SubsystemResponse:
        """Execute a command and return a structured response."""


class IMonitorable(ABC):
    """Interface for metric exposure and management."""

    @abstractmethod
    def get_metrics(self) -> dict[str, Any]:
        """Return a full metrics snapshot."""

    @abstractmethod
    def get_metric(self, metric_name: str) -> Any:
        """Return a single metric by name."""

    @abstractmethod
    def reset_metrics(self) -> bool:
        """Reset metric values to subsystem defaults."""


class IObservable(ABC):
    """Interface for pub/sub event observation."""

    @abstractmethod
    def subscribe(self, event_type: str, callback: callable) -> str:
        """Subscribe callback to an event type and return subscription ID."""

    @abstractmethod
    def unsubscribe(self, subscription_id: str) -> bool:
        """Remove a callback subscription by ID."""

    @abstractmethod
    def emit_event(self, event_type: str, data: Any) -> int:
        """Emit event payload and return number of listeners notified."""
