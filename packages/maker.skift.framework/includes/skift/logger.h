#pragma once

/* Copyright © 2018-2019 MAKER.                                               */
/* This code is licensed under the MIT License.                               */
/* See: LICENSE.md                                                            */

#include <skift/generic.h>

#ifndef __FILENAME__
    #define __FILENAME__ "NONE"
#endif

typedef enum
{
    LOG_OFF = 9,
    LOG_FATAL = 8,
    LOG_SEVERE = 7,
    LOG_ERROR = 6,
    LOG_WARNING = 5,
    LOG_INFO = 4,
    LOG_CONFIG = 3,
    LOG_DEBUG = 2,
    LOG_FINE = 1,
    LOG_ALL = 0
} log_level_t;

void sk_logger_setlevel(log_level_t level);
void sk_logger_log(log_level_t level, const char * file, uint line, const char * function, const char * fmt, ...);

#define sk_log(level,va...) sk_logger_log(level, __FILENAME__, __LINE__, __FUNCTION__, va)